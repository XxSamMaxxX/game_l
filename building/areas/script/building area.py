import pygame as p
import os, sys
from controller.behavior.behavior import*
from random import*

sprite_name = 'tail'
sprite_px = 32*2

current_dir = os.path.dirname(__file__)

img_dir = os.path.join(current_dir, '..', 'img')
tail_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))


sprite_name = 'wood'

img_dir = os.path.join(current_dir, '..', 'img')
wood_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))

sprite_name = 'iron'

img_dir = os.path.join(current_dir, '..', 'img')
iron_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))

wheat = 'iron'

img_dir = os.path.join(current_dir, '..', 'img')
wheat_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))

wood = []
iron = []
wheat = []

class wheats(behaviors):
    def __init__(self,x,y):
        super().__init__()
        self.x, self.y = x+12, y+12
        self.image = p.transform.scale(wheat_image, (32, 32))
        self.rect = p.Rect(self.x, self.y, 32, 32)

class irons(behaviors):
    def __init__(self,x,y):
        super().__init__()
        self.x, self.y = x+12, y+12
        self.image = p.transform.scale(iron_image, (32, 32))
        self.rect = p.Rect(self.x, self.y, 32, 32)

class woods(behaviors):
    def __init__(self,x,y):
        super().__init__()
        self.x, self.y = x+12, y+12
        self.image = p.transform.scale(wood_image, (32, 32))
        self.rect = p.Rect(self.x, self.y, 32, 32)


class tails(behaviors):
    area_x = 0
    area_y = 0
    limit_x = 1
    limit_y = 0
    revers = 0
    def __init__(self):
        super().__init__()
        self.x, self.y = tails.area_x, tails.area_y
        self.image = p.transform.scale(tail_image, (sprite_px, sprite_px))
        self.rect = p.Rect(self.x, self.y, sprite_px, sprite_px)
        tails.limit_x += 1
        tails.limit_y +=1
        self.wood = False
        self.iron = False
        self.wheat = False
        spawn_rsc = randint(0,20)
        
        if spawn_rsc == 1:
            wood.append(woods(self.x, self.y))
            self.wood = True
        elif spawn_rsc == 2:
            iron.append(irons(self.x, self.y))
            self.iron = True
        elif spawn_rsc == 3:
            wheat.append(wheats(self.x, self.y))
            self.wheat = True

        if tails.limit_x == 1: 
            tails.area_x += sprite_px
            tails.area_y += 14*2
            tails.area_x -= 10*2
        if tails.limit_x == 2:
            tails.area_y -= 26*2

        if tails.limit_x == 3:
            tails.area_x += 24*2
            tails.area_y += 12*2
            tails.limit_x = 0
        
        if tails.limit_y == 63:
            if tails.revers == 0:
                tails.limit_x =0
                tails.revers = 1
                tails.area_y += 25*2
            else:
                tails.limit_x =1
                tails.revers = 0
                tails.area_y += 53*2
            
            tails.area_x = 0
            tails.limit_y = 0