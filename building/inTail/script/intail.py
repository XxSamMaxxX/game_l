
import config
from building.buildings.script.buildings import*
fortress_list = []
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
                self.image = image[0]
        

InTails_item = [InTails_items() for _ in range(6)]

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

time_since_last_execution = 0
execution_interval = 100

def intails(world_tail_index):
    global time_since_last_execution, execution_interval
    if buildings:
        for i in buildings:
            i.draw()
    menu = True
    while menu:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        
            if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                for i in InTails_item:
                    if i.rect.collidepoint(mouse_x, mouse_y):
                        create_build(i.category, i.index)
                        time_since_last_execution = 0
                        
                if tail_menu.btn_exit.collidepoint(mouse_x, mouse_y):
                    menu = False
                    tail_menu.house = False
                elif tail_menu.btn_house.collidepoint(mouse_x, mouse_y):
                    tail_menu.house = not tail_menu.house



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
                    world_tail[world_tail_index].draw()
                    for x in buildings:
                        if x.place:
                            x.draw()
                    i.draw()

                    time_since_last_execution += config.clock.get_time()

                    if time_since_last_execution >= execution_interval:
                        if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                            i.place = True
                    
        if tail_menu.house:
            for i in InTails_item:
                i.select_icon(1)
                i.draw()

        p.display.flip()
        config.clock.tick(config.FPS)
