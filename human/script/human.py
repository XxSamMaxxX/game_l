
import config
from building.buildings.script.buildings import*



current_dir = os.path.dirname(__file__)



human_list = []


radius = 3 

class Humans(behaviors):
    


    def __init__(self):
        self.sprite_px = 16
        self.target_x = None
        self.target_y = None
        self.image = img_exact('human',current_dir)
        self.x = randint(1000, 1300)
        self.y = randint(600, 800)
        self.prof = 'cival'
        self.workspace = 0
        self.speed = 1

        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)     


    def generate_random_target(self):
        x, y = randint(730, 1350),randint(195, 863)
        self.target_x = x
        self.target_y = y
        self.speed = 1

            
    def generate_job_target(self):
        if self.prof == 'farmer':
            if self.x == self.workspace[0] and self.y == self.workspace[1]:
            
                x, y = randint(500, 501),randint(350, 351)
                self.target_x = x
                self.target_y = y
                self.speed = 1
                
            else:
                self.target_x = self.workspace[0]
                self.target_y = self.workspace[1]

                self.speed = 1

    def move_towards_target(self):

        if self.prof == 'cival':
            if self.target_x is None or self.target_y is None:
                self.generate_random_target()
                
            else:
            

                self.pixel_colors = []


                for x_offset in range(-radius, radius + 1):
                    for y_offset in range(-radius, radius + 1):
                        x = self.x + x_offset
                        y = self.y + y_offset
            
                        self.pixel_color = config.screen.get_at((x, y))
                        self.pixel_colors.append(self.pixel_color)

                if (0, 0, 0, 255) in self.pixel_colors:
                    self.speed = 0
                    self.pixel_colors = []
                    self.generate_random_target()
            
                if self.x < self.target_x:
                    self.x += self.speed
                elif self.x > self.target_x:
                    self.x -= self.speed

                if self.y < self.target_y:
                    self.y += self.speed
                elif self.y > self.target_y:
                    self.y -= self.speed

                self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)

                # Проверяем достижение цели
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
                    self.target_x = None
                    self.target_y = None