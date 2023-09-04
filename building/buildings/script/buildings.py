from controller.behavior.behavior import*




current_dir = os.path.dirname(__file__)

images =  img_all(current_dir)

buildings = []

class Buildings(behaviors):
    def __init__(self, image,fortress_index):
        super().__init__()
        self.sprite_px = 64
        self.x, self.y = 0, 0
        self.place = False
        self.image = image
        self.index = fortress_index
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)
    
def create_build(category, index,fortress_index):
    if category == 1:
        if index == 1:
            image = images[0]
    buildings.append(Buildings(image, fortress_index))

