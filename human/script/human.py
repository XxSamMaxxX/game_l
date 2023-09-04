
import config
from building.buildings.script.buildings import*


current_dir = os.path.dirname(__file__)


human_list = []




class Humans(behaviors):

    def __init__(self):
        self.x = randint(700, 700 + ((128 * 6) - 100))
        self.y = randint(200, 200 + ((128 * 6) - 100))

        

        self.sprite_px = 16
        self.map_width = 128*5
        self.map_height = 128*5
        self.target_x = None
        self.target_y = None
        self.image = img_exact('human',current_dir)
        self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)

    def generate_random_target(self):
        self.target_x = randint(700, 700+ (128*6)-100)
        self.target_y = randint(200, 200+ (128*6) - 100)

    def move_towards_target(self):
        if self.target_x is None or self.target_y is None:
            self.generate_random_target()
        else:
            # Вычисляем направление движения к цели (self.target_x, self.target_y)
            if self.x < self.target_x:
                self.x += 1
            elif self.x > self.target_x:
                self.x -= 1

            if self.y < self.target_y:
                self.y += 1
            elif self.y > self.target_y:
                self.y -= 1
            self.rect = p.Rect(self.x, self.y, self.sprite_px, self.sprite_px)
            # Проверяем достижение цели
            if self.x == self.target_x and self.y == self.target_y:
                self.target_x = None
                self.target_y = None
