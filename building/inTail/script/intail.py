
import config
from building.buildings.script.buildings import*
from human.script.human import*
from building.inTail.script.generation import*

current_dir = os.path.dirname(__file__)


world_tail = []

class InTails_items_icon(behaviors):

    slot_category_icon = img_all_folder('slot_icon', current_dir)
    craft_buildings = {
        'foresters_house' : img_exact_modify('buildings','img','craft','foresters_house', current_dir),
        'mine' : img_exact_modify('buildings','img','craft','mine', current_dir) 
    }

    production_buildings = {
        'forge' : img_exact_modify('buildings','img','production','forge', current_dir),
        'sawmill' : img_exact_modify('buildings','img','production','sawmill', current_dir) 
    }

    farming_buildings = {
        'mill' : img_exact_modify('buildings','img','farming','mill', current_dir) 
    }

    social_buildings = {
        'stock' : img_exact_modify('buildings','img','social','stock', current_dir) 
    }

    def __init__(self,x,y,index):
        super().__init__()
        self.rect = p.Rect(x,y, 180,180)
        self.index = index
        if self.index == 1:
            try:
                self.image = InTails_items_icon.slot_category_icon[0]
            except:
                self.image = InTails_items_icon.slot_category_icon[5]

        elif self.index == 2:
            try:
                self.image = InTails_items_icon.slot_category_icon[1]
            except:
                self.image = InTails_items_icon.slot_category_icon[5]
        elif self.index == 3:
            try:
                self.image = InTails_items_icon.slot_category_icon[2]
            except:
                self.image = InTails_items_icon.slot_category_icon[5]
        elif self.index == 4:
            try:
                self.image = InTails_items_icon.slot_category_icon[3]
            except:
                self.image = InTails_items_icon.slot_category_icon[5]
        elif self.index == 5:
            try:
                self.image = InTails_items_icon.slot_category_icon[4]
            except:
                self.image = InTails_items_icon.slot_category_icon[5]


        elif self.index > 5:
            try:
                self.image = InTails_items_icon.slot_category_icon[1]
            except:
                self.image = InTails_items_icon.slot_category_icon[3]         


def refresh_slot_icon(index):
        
    for slot in InTails_item:
        if slot.index > 5:
            slot.draw()

    for icon in InTails_items_icons:
        if index == 1:
            if icon.index == 6:
                try:
                    icon.rect.x = 350
                    icon.rect.y = 15
                    icon.image = p.transform.scale(InTails_items_icon.craft_buildings['foresters_house'], (120,120))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]
            if icon.index == 7:
                try:
                    icon.rect.x = 525
                    icon.rect.y = 30
                    icon.image = p.transform.scale(InTails_items_icon.craft_buildings['mine'], (100,100))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]
            icon.draw()

        elif index == 2:
            if icon.index == 6:
                try:
                    icon.rect.x = 365
                    icon.rect.y = 15
                    icon.image = p.transform.scale(InTails_items_icon.farming_buildings['mill'], (120,120))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]

            icon.draw()

        elif index == 3:
            if icon.index == 6:
                try:
                    icon.rect.x = 360
                    icon.rect.y = 30
                    icon.image = p.transform.scale(InTails_items_icon.social_buildings['stock'], (100,100))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]
            icon.draw()

        elif index == 4:
            if icon.index == 6:
                try:
                    icon.rect.x = 360
                    icon.rect.y = 30
                    icon.image = p.transform.scale(InTails_items_icon.production_buildings['forge'], (90,90))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]
            if icon.index == 7:
                try:
                    print(icon.rect.x)
                    icon.rect.x = 510
                    icon.image = p.transform.scale(InTails_items_icon.production_buildings['sawmill'], (120,120))
                except:
                    icon.image = InTails_items_icon.slot_category_icon[5]
            icon.draw()

            
        
class InTails_items(behaviors):
    area_x = 20
    area_y = 200
    limit = 0
    


    def __init__(self):
        super().__init__()
        self.x, self.y = InTails_items.area_x, InTails_items.area_y
        self.image = img_exact('inerface_slot', current_dir)
        self.rect = p.Rect(self.x, self.y, 135, 135)
        
        InTails_items.limit+=1
        if InTails_items.limit <= 4:
            InTails_items.area_y += 165
        elif InTails_items.limit == 5:
            InTails_items.area_y = 15
            InTails_items.area_x = 340
        else:
            InTails_items.area_x += 165
        self.index = InTails_items.limit
        InTails_items_icons.append(InTails_items_icon(self.x, self.y, self.index))
    


class InTails(behaviors):
    left_area = p.Rect(0, 0, 170,1080)
    up_area = p.Rect(0, 0, 1920,160)
    down_area = p.Rect(0, 1030, 1920,160)
    right_area = p.Rect(1580, 0, 500, 1080)
    def __init__(self, image, index, biome):
        super().__init__()
        self.index = index
        self.photo =  img_exact('intail', current_dir)
        self.image = p.transform.scale(self.photo, (1420, 865))
        self.rect = p.Rect(170, 160, 1410, 865)
        self.biome = biome
        intail_gen = Intail_generation(self.biome)
        self.trees_list = intail_gen.trees_list
        self.stones_list = intail_gen.stones_list
        self.prop = self.trees_list + self.stones_list
         


class InTails_menu(behaviors):
    def __init__(self):
        super().__init__()
        self.image = img_exact('interface_bg', current_dir)
        self.rect = p.Rect(0, 0, 1920, 1080)
        self.btn_exit = p.Rect(1800, 25, 100, 100)




tail_menu = InTails_menu()
InTails_items_icons = []
InTails_item = [InTails_items() for _ in range(11)]


my_buildings =[]
def human_resourse(fortress_index):
    for t in world_tail:
        if t.index == fortress_index:
            trees_list = t.trees_list

    return trees_list


def intails(fortress_index):
    category = 0
    global my_buildings

    human_list = [Humans(fortress_index) for _ in range(2)]
    
    my_buildings = []
    menu = True
    time_since_last_execution = 0
    execution_interval = 100


    tail_menu.draw()
    for slot in InTails_item:
        slot.draw()

    for icon in InTails_items_icons:
        icon.draw()

    for t in world_tail:
        if t.index == fortress_index:

            my_tail = t
           

            t.draw()


    for obj in my_tail.prop:
        for obj_next in my_tail.prop:
            if obj_next != obj:
                if obj_next.rect.colliderect(obj.rect):
                    my_tail.prop.remove(obj_next)

    if buildings:
        for i in buildings:
            if fortress_index == i.index:
                my_buildings.append(i)
                i.draw()
                

    timer_event = p.USEREVENT + 1
    p.time.set_timer(timer_event, 2000)
    working_check_list = []


    while menu:
     
        my_tail.draw()

        for human in human_list:
            human.move_towards_target()
            human.draw()

        if my_buildings:
            for i in my_buildings:
                    if i.place:
                        i.draw()
                    else:
                        if not (i.rect.colliderect(my_tail.down_area) or
                            i.rect.colliderect(my_tail.up_area) or
                            i.rect.colliderect(my_tail.left_area) or
                            i.rect.colliderect(my_tail.right_area)):
                            i.draw()
        
        for tree in Humans.map_resourse[fortress_index]:
            tree.draw()
            
        for event in p.event.get():
            if event.type == p.QUIT: p.quit(); sys.exit()        
            elif event.type == timer_event:
                if working_check_list:
                    time_out = randint(1, 2)
                    if time_out == 1:
                        human = choice(human_list)
                        if human.prof == 'cival':
                            for j in working_check_list:
                                if j[0] == 'farmer':
                                    image = p.transform.scale(Humans.photo[1], (16,16)) 
                                elif j[0] == 'forester':
                                    image = p.transform.scale(Humans.photo[0], (16,16)) 
                                else:
                                    image = p.transform.scale(Humans.photo[2], (16,16)) 
                                human.prof = j[0]
                                human.image = image
                                human.workspace = (j[1]+120, j[2]+120)
                                working_check_list.remove(j)
                                break
                        

            elif event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos

                for i in InTails_item: 
                    if i.rect.collidepoint(mouse_x, mouse_y) and i.index < 6:
                        refresh_slot_icon(i.index)
                        category = i.index
                        time_since_last_execution = 0
                    elif i.rect.collidepoint(mouse_x, mouse_y) and i.index > 5:
                        time_since_last_execution = 0
                        job,employees, build = create_build(category,i.index, fortress_index)
                        my_buildings.append(build)
                        
            elif event.type == p.MOUSEMOTION:
                if my_buildings:
                    for i in my_buildings:
                        if not i.place:
                            mouse_x, mouse_y = event.pos
                            new_x = mouse_x - 40
                            new_y = mouse_y - 80           
                            i.x, i.y = new_x, new_y
                            i.rect.x, i.rect.y = new_x, new_y                            



                       
                            
                time_since_last_execution += config.clock.get_time()

            if event.type == p.MOUSEBUTTONDOWN and event.button == 1:
                if time_since_last_execution >= execution_interval:
                    print(1)
                    for i in my_buildings:
                        if not i.place:
                            if not (i.rect.colliderect(my_tail.down_area) or
                                i.rect.colliderect(my_tail.up_area) or
                                i.rect.colliderect(my_tail.left_area) or
                                i.rect.colliderect(my_tail.right_area)):
                                i.place = True
                                for _ in range(employees):
                                    working_check_list.append((job, i.x, i.y))


         
        
        
        p.display.flip()
        config.clock.tick(config.FPS)
