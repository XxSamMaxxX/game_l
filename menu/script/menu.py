from controller.behavior.behavior import*


current_dir = os.path.dirname(__file__)

img_dir = os.path.join(current_dir, '..', 'img')

menu_image = img_animation('bg', current_dir)
class Menu(behaviors):
    def __init__(self):
        super().__init__()
        self.x, self.y = 0, 0
        self.image = p.transform.scale(menu_image[0], (1920, 1080))
        self.index = -1
        self.max_index = len(menu_image)-1
        self.rect = p.Rect(self.x, self.y, 1920, 1080)
        self.btn_play_rect = p.Rect(480,450, 960,170)
    
    def animation_play(self):
        if self.index < self.max_index:
            self.index+=1
            self.image = p.transform.scale(menu_image[self.index], (1920, 1080))
        else:
            self.index = 0
    def btn_play(self, mouse_x, mouse_y):
        if self.btn_play_rect.collidepoint(mouse_x, mouse_y):
            return True