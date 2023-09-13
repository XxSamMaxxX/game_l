from controller.behavior.behavior import*
import building.inTail.script.intail as inTail
'''
Индексы построек:

6 - Мельница

'''


current_dir = os.path.dirname(__file__)

craft_image = img_all_folder_modify('foresters_house','craft', current_dir)
craft_image.extend(img_all_folder_modify('mine','craft', current_dir))

farming_image = img_all_folder_modify('mill','farming', current_dir)

production_image = img_all_folder_modify('forge','production', current_dir)
production_image.extend(img_all_folder_modify('sawmill','production', current_dir))

social_image = img_all_folder_modify('stock','social', current_dir)

images =  img_all(current_dir)
#images.extend(craft_image)
#images.extend(farming_image)
buildings = []

class Buildings(behaviors):
    my_id = -1
    def __init__(self, image,fortress_index=-1, employees=-1, job_title=0, name='', x=0,y=0):
        super().__init__()
        self.sprite_px = 64
        self.x, self.y = x, y
        if x != 700:
            self.place = True
        else:
            self.place = False
        self.image = image
        self.index = fortress_index
        self.my_id = Buildings.my_id
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)
        self.employees = employees
        self.name = name
        self.resourse = 0
        Buildings.my_id +=1
    
def create_build(category,index,fortress_index):
    if category == 1:
        if index == 6:
            image = p.transform.scale(craft_image[0], (80,80))
            employees = 1      
            job_title = 'forester'
            name = 'Forester home'    
        elif index == 7:
            image = p.transform.scale(craft_image[1], (80,80))
            employees = 1      
            job_title = 'miner'
            name = 'Mine'    
    if category == 2:
        if index == 6:
            image = p.transform.scale(farming_image[0], (120,120))
            employees = 2
            job_title = 'farmer'
            name = 'Mill'
    if category == 3:
        if index == 6:
            image = p.transform.scale(social_image[0], (80,80))
            employees = 4
            job_title = 'stocker'
            name = 'Stock'     
    if category == 4:
        if index == 6:
            image = p.transform.scale(production_image[0], (80,80))
            employees = 1
            job_title = 'blacksmith'
            name = 'Forge'   
        elif index == 7:
            image = p.transform.scale(production_image[1], (80,80))
            employees = 1
            job_title = 'Woodworker'
            name = 'Sawmill' 
    buildings.append(Buildings(image, fortress_index, employees, -1,name,700,700))

    return job_title, employees, buildings[-1]

def create_adjoining(building, index,x,y):
    if building == 'farmer':
        image = p.transform.scale(images[2],(16,16))
        name = 'Ferma'
        buildings.append(Buildings(image, index, -1, -1 ,name,x,y))
        inTail.my_buildings.append(buildings[-1])

    if building == 'forester':
        image = images[1]
        name = 'Tree'
        buildings.append(Buildings(image, index, -1, -1 ,name,x,y))
        inTail.my_buildings.append(buildings[-1])
        return buildings[-1]
    

