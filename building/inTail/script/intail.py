from controller.behavior.behavior import*
import config
fortress_list = []
current_dir = os.path.dirname(__file__)
world_tail = []

class InTails_items(behaviors):
    area_x = 200
    area_y = 20
    limit = 0
    image = img_exact('slot_item',current_dir)
    def __init__(self):
        super().__init__()
        self.x, self.y = InTails_items.area_x, InTails_items.area_y
        self.image =  InTails_items.image
        self.rect = p.Rect(self.x, self.y, 100, 100)
        InTails_items.limit+=1
        if InTails_items.limit != 6:
            InTails_items.area_x += 208
        else:
            InTails_items.area_y += 202
            InTails_items.area_x = 200
            InTails_items.limit = 0

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


def intails():
    menu = True
    while menu:
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
        
            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                if tail_menu.btn_exit.collidepoint(mouse_x, mouse_y):
                    menu = False
                elif tail_menu.btn_house.collidepoint(mouse_x, mouse_y):
                    tail_menu.house = not tail_menu.house
        if tail_menu.house:
            for i in InTails_item:
                i.draw()

        #p.draw.rect(config.screen, config.BLACK, tail_menu.btn_house)
        p.display.flip()
        config.clock.tick(config.FPS)
