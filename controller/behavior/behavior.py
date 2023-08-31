import config 
from controller.module.module import*


class behaviors:
    
    def __init__(self):
        pass
        
    def draw(self, camera):  # Передаем экземпляр камеры
        pass
    
def collide(who, whot):
    if who.rect.colliderect(whot):
        return True
