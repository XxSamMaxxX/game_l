
import config
from building.buildings.script.buildings import*
from human.script.human import*


current_dir = os.path.dirname(__file__)


world_tail = []

image = img_all_folder('slot_icon',current_dir)


class InTails_items(behaviors):
    area_x = 460
    area_y = 5
    limit = 0
    
    def __init__(self):
        super().__init__()
        self.x, self.y = InTails_items.area_x, InTails_items.area_y
        self.image = image[-1]
        self.rect = p.Rect(self.x, self.y, 190, 190)
        self.category = 0
        self.visible = False

        InTails_items.limit+=1
        if InTails_items.limit < 6:
            InTails_items.area_x += 208
        else:
            InTails_items.area_y += 202
            InTails_items.area_x = 200
            InTails_items.limit = 0

        self.index = InTails_items.limit


    def select_icon(self, cat):
        if cat == 1:
            if self.index == 1:
                self.category = 1
                self.image = image[1]
            if self.index == 2:
                self.category = 1
                self.image = image[0]        


class InTails(behaviors):
    def __init__(self, image, index):
        super().__init__()
        self.sprite_px = 128*6
        self.x, self.y = 700, 200
        self.index = index
        
        self.image = p.transform.scale(image, (self.sprite_px, self.sprite_px)) 
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)



class InTails_menu(behaviors):
    def __init__(self):
        super().__init__()
        self.x, self.y = 0, 0
        self.image = img_exact('bg',current_dir)
        self.rect = p.Rect(self.x, self.y, 1920, 1080)
        self.btn_exit = p.Rect(1800, 25, 100, 100)
        self.btn_house = p.Rect(80, 55, 100, 100)
        self.house = False



tail_menu = InTails_menu()
InTails_item = [InTails_items() for _ in range(6)]





def intails(fortress_index):
    human_list = [Humans() for _ in range(10)]

    buffer_surface = p.Surface((config.WIDTH, config.HEIGHT))

    menu = True
    time_since_last_execution = 0
    execution_interval = 100


    tail_menu.draw()
    for t in world_tail:
        if t.index == fortress_index:
            t.draw()

    for human in human_list:
        human.draw1(buffer_surface)
            

    if buildings:
        for i in buildings:
            if fortress_index == i.index:
                i.draw()
                

    config.screen.blit(buffer_surface, (0, 0))
    
    while menu:

        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()

            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                for i in InTails_item:
                    if i.visible == True:
                        if i.rect.collidepoint(mouse_x, mouse_y):
                            time_since_last_execution = 0
                            create_build(i.category, i.index, fortress_index)
                        
                if tail_menu.btn_exit.collidepoint(mouse_x, mouse_y):
                    menu = False
                    tail_menu.house = False

                if tail_menu.btn_house.collidepoint(mouse_x, mouse_y):
                    tail_menu.house = not tail_menu.house

            elif event.type == p.MOUSEMOTION:
                if buildings:
                    for i in buildings:
                        if not i.place:
                            mouse_x, mouse_y = event.pos
                            new_x = mouse_x - 100
                            new_y = mouse_y - 100
                            # Перемещение объекта и обработка интервала времени
                            i.x, i.y = new_x, new_y
                            i.rect.x, i.rect.y = new_x, new_y

                            tail_menu.draw()
                            for t in world_tail:
                                if t.index == fortress_index:
                                    t.draw()

                            i.draw()

                            for x in buildings:
                                if x.place and fortress_index == x.index:
                                    x.draw()

                            
                time_since_last_execution += config.clock.get_time()
            if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                
                if time_since_last_execution >= execution_interval:
                    for i in buildings:
                        if not i.place:
                            i.place = True

                    
        if tail_menu.house:
            for i in InTails_item:
                i.visible = True
                i.select_icon(1)
                i.draw()
        else:
            for i in InTails_item:
                i.visible = False

        for human in human_list:
            human.move_towards_target()
            buffer_surface.fill((0,0,0,0))
            human.draw1(buffer_surface)
            
        p.display.flip()
        config.clock.tick(config.FPS)
