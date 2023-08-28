from controller.behavior.behavior import*
from controller.path_controller.path_obj import*

sprite_px = 64

current_dir = os.path.dirname(__file__)

waters = 0
sands = 0
stones = 0
forests = 0

COUNT_BIOME = 0
land_to_water_ratio = 70

def biom_generate(count_tails):
    global COUNT_BIOME, waters, sands, stones, forests
    x = int((((count_tails * 100) / land_to_water_ratio)/2))
    forests = x
    x = count_tails - x

    wtr = int(x * 0.33)
    snd = int(x * 0.33)
    stn = int(x * 0.33)
    limit_list = [wtr,snd,stn]
  
    oper = 0
    for count in limit_list:
        oper +=1
        for _ in range(count):
            COUNT_BIOME +=1

        if oper == 1:
            waters = COUNT_BIOME
        elif oper == 2:
            sands = COUNT_BIOME
        elif oper == 3:
            stones = COUNT_BIOME
            
        COUNT_BIOME = 0
# 0-лес 1-песок 2-камень 3-вода
def image_tail_choice():
    global waters, sands, stones, forests
    rnd = randint(1,20)

    if rnd >=1 and rnd <=3:
        if waters >= 1:
            ind,img = img_any('water', current_dir)
            waters-=1
        else:
            ind,img = img_any('forest', current_dir) 
        
    elif rnd >=4 and rnd <=9:
        if stones >= 1:
            ind,img = img_any('stone', current_dir)
            stones-=1
        else:
            ind,img = img_any('forest', current_dir)

    elif rnd >=10 and rnd <=17:
        if sands >= 1:
            ind,img = img_any('sand', current_dir)
            sands-=1
        else:
            ind,img = img_any('forest', current_dir) 
            
    else:
        ind,img = img_any('forest', current_dir)
        
    image_index = ind

    image_filename = os.path.basename(image_index)
    full_image_path = os.path.join(img_dir, image_filename)
    return img,full_image_path
            
class tails(behaviors):
    area_x = -43
    area_y = 0
    limit_x = 0
    limit_y = 0
    revers = 0
    two_block = 1
    count = 0

    def __init__(self,saved = 0,x=0,y=0,img_p =0):
        super().__init__()
        if saved == 0:
            self.x, self.y = tails.area_x, tails.area_y
            img, self.full_image_path = image_tail_choice()
            self.image = p.transform.scale(img, (sprite_px, sprite_px))
            self.rect = p.Rect(self.x, self.y, sprite_px, sprite_px)
            self.wood = False
            self.iron = False
            self.wheat = False
            self.metal = False
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
            elif spawn_rsc == 4:
                wheat.append(metals(self.x, self.y))
                self.metal = True

            tails.limit_x+=1

            if tails.limit_x < 69:
                if tails.count == 0:
                    tails.area_x += 43
                    tails.revers += 1
                    tails.count = 1

                elif tails.count == 1 and tails.revers == 3:
                    tails.area_x += 43
                    tails.area_y -= 32
                    tails.revers = 0
                    tails.count = 0

                if tails.revers == 1:

                    if tails.two_block == 1:
                        tails.area_y -=32
                        tails.two_block += 1
                    elif tails.two_block == 2:
                        tails.area_y += 64
                        tails.revers = 3
                        tails.two_block = 1

                        if tails.limit_x == 2 and tails.limit_y != 0:
                            tails.area_x -= 43

            else:

                if tails.revers == 3:
                    tails.area_x = -43
                    tails.area_y += 32 
                    tails.limit_x = 0       
                    tails.count  = 1    
                    tails.revers = 1
                    tails.two_block += 1
                else:
                    tails.area_x = -43 
                    tails.area_y += 96  
                    tails.limit_x = 0                        
                    tails.count  = 1
                    tails.revers = 3               
                    tails.two_block += 1

                tails.limit_y = 1
        else:
            self.x, self.y = x, y
            img = p.image.load(img_p)
            self.image = img
            self.rect = p.Rect(x, y, sprite_px, sprite_px)
            
def info(mouse_x,mouse_y):
    for t in tail:
        if t.rect.collidepoint(mouse_x, mouse_y):
            if t.wood:
                print("Наличие дерева на ячейке:", t.wood)
            else:
                print("Наличие дерева на ячейке:", t.wood)


count_tails = 826
biom_generate(count_tails)
tail = [tails() for _ in range(count_tails)]