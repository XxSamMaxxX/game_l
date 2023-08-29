from controller.behavior.behavior import*

sprite_name = 'metal'

sprite_px = 32*2

current_dir = os.path.dirname(__file__)

img_dir = os.path.join(current_dir, '..', 'img')
metal_image = p.image.load(os.path.join(img_dir, sprite_name +'.png'))


metal = []

class metals (behaviors):
    def __init__(self,x,y):
        super().__init__()
        self.sprite_px = sprite_px
        self.x, self.y = x+12, y+12
        self.image = p.transform.scale(metal_image, (32, 32))
        self.rect = p.Rect(self.x, self.y, 32, 32)


