import config 
from controller.module.module import*


class behaviors:
    
    def __init__(self):
        pass
        
    def draw(self):  # Передаем экземпляр камеры
        config.screen.blit(self.image, self.rect)
    
def collide(who, whot):
    if who.rect.colliderect(whot):
        return True
