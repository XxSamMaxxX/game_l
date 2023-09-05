from controller.behavior.behavior import*




current_dir = os.path.dirname(__file__)

images =  img_all(current_dir)

buildings = []

class Buildings(behaviors):
    def __init__(self, image,fortress_index=-1, employees=-1, job_title=0, name='', x=0,y=0):
        super().__init__()
        self.sprite_px = 64
        self.x, self.y = x, y
        if x != 0:
            self.place = True
        else:
            self.place = False
        self.image = image
        self.index = fortress_index
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)
        self.employees = employees
        self.name = name
        
    
def create_build(category, index,fortress_index):
    if category == 1:
        if index == 1:
            image = images[0]
            employees = 1          
        if index == 2:
            image = images[1]
            employees = 2
            job_title = 'farmer'
            name = 'Ferma'

    buildings.append(Buildings(image, fortress_index, employees, -1,name,0,0))

    return job_title, employees

def create_adjoining(building, index,x,y):
    if building == 'farmer':
        image = images[2]
        name = 'Ferma'
        buildings.append(Buildings(image, index, -1, -1 ,name,x,y))
