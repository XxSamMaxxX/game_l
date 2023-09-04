from controller.behavior.behavior import*




current_dir = os.path.dirname(__file__)

images =  img_all(current_dir)

buildings = []

class Buildings(behaviors):
    def __init__(self, image,fortress_index, employees,job_title):
        super().__init__()
        self.sprite_px = 64
        self.x, self.y = 0, 0
        self.place = False
        self.image = image
        self.index = fortress_index
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)
        self.employees = employees
        
    
def create_build(category, index,fortress_index):
    if category == 1:
        if index == 1:
            image = images[0]
            employees = 1          
        if index == 2:
            image = images[1]
            employees = 2
            job_title = 'farmer'
    buildings.append(Buildings(image, fortress_index, employees,job_title))

    return job_title, employees

