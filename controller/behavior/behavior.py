import config 
from controller.module.module import*
from controller.scale.scale import*

class behaviors:
    
    def __init__(self):
        pass
        
    def draw(self):
        scale = get_scale()
        center_x = get_x()
        center_y = get_y()
        scaled_x = int(center_x + (self.x - config.center_x) * scale)
        scaled_y = int(center_y + (self.y - config.center_y) * scale)
        scaled_size = int(self.sprite_px * scale)
        scaled_img = p.transform.scale(self.image, (scaled_size, scaled_size))
        config.screen.blit(scaled_img, (scaled_x, scaled_y))
    
def collide(who, whot):
    if who.rect.colliderect(whot):
        return True
