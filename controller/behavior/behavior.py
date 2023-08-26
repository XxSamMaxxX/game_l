import config
from controller.module.module import*


class behaviors:
    
    def __init__(self):
        pass
        
    def draw(self):
        config.screen.blit(self.image, self.rect)

    def move(self, keys): # Движение 4 стороны
        #Ось Х
        if keys[p.K_LEFT]: self.rect.x -= self.speed      
        elif keys[p.K_RIGHT]: self.rect.x += self.speed
        elif keys[p.K_a]: self.rect.x -= self.speed  
        elif keys[p.K_d]: self.rect.x += self.speed  
        #Ось У
        if keys[p.K_UP]: self.rect.y -= self.speed      
        elif keys[p.K_DOWN]: self.rect.y += self.speed
        elif keys[p.K_w]: self.rect.y -= self.speed  
        elif keys[p.K_s]: self.rect.y += self.speed  
    
def collide(who, whot):
    if who.rect.colliderect(whot):
        return True
