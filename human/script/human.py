
import config
from building.buildings.script.buildings import*

import building.inTail.script.intail as Intails


current_dir = os.path.dirname(__file__)



human_list = []
pole = 0
limit_pole = 0
limit_pole_y = 0
stadia = 0
area_x = 0
area_y = 0
radius = 3 
pole_list = []



class Humans(behaviors):
    trees_resourse = {}
    stones_resourse = {}
    buildings_list = {}
    photo = img_all(current_dir)
    def __init__(self, fortress_index):
        self.sprite_px = 16
        self.target_x = None
        self.target_y = None
        
        self.x = randint(1000, 1300)
        self.y = randint(600, 800)
        self.prof = 'cival'
        self.workspace = 0
        self.my_work_house = -1
        self.speed = 1
        self.index = fortress_index
        self.mission = 0
        self.my_target = 0
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)  
        self.image = p.transform.scale(Humans.photo[2], (16,16)) 
        self.resourse = 0



        if fortress_index not in Humans.trees_resourse:
            Humans.trees_resourse[fortress_index] = Intails.trees_resourse(fortress_index)
            
        if fortress_index not in Humans.stones_resourse:
            Humans.stones_resourse[fortress_index] = Intails.stones_resourse(fortress_index)

        if fortress_index not in Humans.buildings_list:
        
            Humans.buildings_list[fortress_index] = Intails.buildings_check()

            
    def generate_random_target(self):
        x, y = randint(190, 1400),randint(170, 855)
        self.target_x = x
        self.target_y = y
        self.speed = 1


    def generate_job_target(self):
        global pole, area_x, area_y, limit_pole, stadia,limit_pole_y
        if self.prof == 'farmer':

            if stadia == 0:
                area_x = self.workspace[0] - 170 
                area_y = self.workspace[1] - 50
                stadia = 1
            if self.x == self.workspace[0] and self.y == self.workspace[1]:
                if pole <=5:
                    pole+=1
                    if limit_pole_y <=1:
                        if limit_pole <=2:
                            area_x += 16
                            limit_pole+=1
                        else:
                            area_x = self.workspace[0] - 170 
                            area_y += 16
                            area_x += 16
                            limit_pole = 1
                            limit_pole_y += 1

                    self.target_x = area_x
                    self.target_y = area_y
                    self.speed = 1
                    self.mission = 1
                                
                    print('Иду делать поле!')
                else:
                    x, y = choice(pole_list)
                    self.target_x = x
                    self.target_y = y
                    self.speed = 1
                    self.mission = 0
                    print('Все поля сделаны')
            else:
                self.target_x = self.workspace[0]
                self.target_y = self.workspace[1]
                self.mission = 0
                self.speed = 1
                print('Иду в мельницу')

        elif self.prof == 'forester':
           
            if self.x == self.workspace[0] and self.y == self.workspace[1]:
                if self.mission == 3:
                    
                    
                    if Humans.buildings_list[self.index].my_id == self.my_work_house:
                        Humans.buildings_list[self.index].resourse += self.resourse
                        self.resourse =0
                        

                if len(Humans.trees_resourse[self.index]) < 3:
                    x, y = randint(190, 1400),randint(170, 855)
                    self.target_x = x
                    self.target_y = y
                    self.speed = 1
                    self.mission = 1
                    
                                
                    print('Иду садить дерево!')
                else:
                    obj = choice(Humans.trees_resourse[self.index])
                    x,y = obj.x, obj.y
                    self.target_x = x
                    self.target_y = y
                    self.speed = 1
                    self.mission = 2
                    self.my_target = obj
                    print('Иду рубить дерево!')




            else:
                self.target_x = self.workspace[0]
                self.target_y = self.workspace[1]
                self.speed = 1
                print('Иду в хижину')

        elif self.prof == 'miner':
            if self.x == self.workspace[0] and self.y == self.workspace[1]:
                if len(Humans.stones_resourse[self.index]) < 3:
                    x, y = randint(190, 1400),randint(170, 855)
                    self.target_x = self.workspace[0]+50
                    self.target_y = self.workspace[1]
                    self.speed = 1
                    self.mission = 1
                    
                                
                    print('Иду глубоко в шахту!')
                else:
                    obj = choice(Humans.stones_resourse[self.index])
                    x,y = obj.x, obj.y
                    self.target_x = x
                    self.target_y = y
                    self.speed = 1
                    self.mission = 2
                    self.my_target = obj
                    print('Иду долбить камень!')
            else:
                self.target_x = self.workspace[0]
                self.target_y = self.workspace[1]
                self.mission = 0
                self.speed = 1
                print('Иду в шахту')

    def move_towards_target(self):

        if self.prof == 'cival':
            if self.target_x is None or self.target_y is None:
                self.generate_random_target()
                
            else:
            
                if self.x < self.target_x:
                    self.x += self.speed
                elif self.x > self.target_x:
                    self.x -= self.speed

                if self.y < self.target_y:
                    self.y += self.speed
                elif self.y > self.target_y:
                    self.y -= self.speed

                self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)

               
                if self.x == self.target_x and self.y == self.target_y:
                    self.target_x = None
                    self.target_y = None
        
        if self.prof == 'farmer':
                if self.target_x is None or self.target_y is None:
                    self.generate_job_target()

                if self.x < self.target_x:
                    self.x += self.speed
                elif self.x > self.target_x:
                    self.x -= self.speed

                if self.y < self.target_y:
                    self.y += self.speed
                elif self.y > self.target_y:
                    self.y -= self.speed

                self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)                
                
                if self.x == self.target_x and self.y == self.target_y:
                    if self.mission == 1:
                        create_adjoining(self.prof,self.index, self.x, self.y)
                        self.target_x = None
                        self.target_y = None
                        self.mission = 0
                        pole_list.append((self.x, self.y))
                        print('Миссию выполнил')
                        
                    else:
                        self.target_x = None
                        self.target_y = None
                        print('Нет миссий')

        if self.prof == 'forester':
                if self.target_x is None or self.target_y is None:
                    self.generate_job_target()

                if self.x < self.target_x:
                    self.x += self.speed
                elif self.x > self.target_x:
                    self.x -= self.speed

                if self.y < self.target_y:
                    self.y += self.speed
                elif self.y > self.target_y:
                    self.y -= self.speed

                self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)                
                
                if self.x == self.target_x and self.y == self.target_y:
                    if self.mission == 1:
                        
                        Humans.trees_resourse[self.index].append(create_adjoining(self.prof,self.index, self.x, self.y))
                        self.target_x = None
                        self.target_y = None
                        
                        print('Миссию выполнил')
                    elif self.mission == 2:
                        Humans.trees_resourse[self.index].remove(self.my_target)
                        
                        self.target_x = None
                        self.target_y = None
                        self.mission = 3
                        print('Миссию выполнил')
                        self.resourse += 1
                        
                    else:
                        self.target_x = None
                        self.target_y = None
                        print('Нет миссий')

        if self.prof == 'miner':
                if self.target_x is None or self.target_y is None:
                    self.generate_job_target()

                if self.x < self.target_x:
                    self.x += self.speed
                elif self.x > self.target_x:
                    self.x -= self.speed

                if self.y < self.target_y:
                    self.y += self.speed
                elif self.y > self.target_y:
                    self.y -= self.speed

                self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)                
                
                if self.x == self.target_x and self.y == self.target_y:
                    if self.mission == 1:
                        
                        
                        self.target_x = None
                        self.target_y = None
                        self.mission = 0
                        print('Миссию выполнил')
                    elif self.mission == 2:
                        Humans.stones_resourse[self.index].remove(self.my_target)
                        
                        self.target_x = None
                        self.target_y = None
                        self.mission = 0
                        print('Миссию выполнил')
                        
                    else:
                        self.target_x = None
                        self.target_y = None
                        print('Нет миссий')