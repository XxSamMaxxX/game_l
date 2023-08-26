from controller.behavior.behavior import*
from controller.path_controller.path_controller import*

current_dir = os.path.dirname(__file__)
img_dir = os.path.join(current_dir, '..', 'img')

sprite_px = 64

image_paths = []
for filename in os.listdir(img_dir):
    if filename.endswith('.png'):
        image_path = os.path.join(img_dir, filename)
        image_paths.append(image_path)

images = []
for image_path in image_paths:
    image = p.image.load(image_path)
    images.append(image)


class tails(behaviors):
    area_x = -43
    area_y = 0
    limit_x = 0
    limit_y = 0
    revers = 0
    two_block = 1
    count = 0
    def __init__(self):
        super().__init__()
        self.x, self.y = tails.area_x, tails.area_y
        self.image = p.transform.scale(choice(images), (sprite_px, sprite_px))
        self.rect = p.Rect(self.x, self.y, sprite_px, sprite_px)
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

                
