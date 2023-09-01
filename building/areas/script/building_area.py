from controller.behavior.behavior import*

fortress_list = []

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

class fortress(behaviors):
    def __init__(self, x_tail, y_tail):
        super().__init__()
        self.sprite_px = sprite_px
        self.x, self.y = x_tail, y_tail
        self.world = False
        self.index = 0
        self.image = p.transform.scale(images[0], (sprite_px, sprite_px))
        self.rect = p.Rect(self.x, self.y, sprite_px, sprite_px)
