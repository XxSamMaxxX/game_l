
import config
from building.buildings.script.buildings import*
from human.script.human import*

current_dir = os.path.dirname(__file__)


class trees(behaviors):
    def __init__(self):
        super().__init__()
        self.sprite_px = 32
        self.x = randint(170, 1410)
        self.y = randint(160, 865)
        self.image = img_exact('tree', current_dir)
        self.rect = p.Rect(self.x, self.y, 32, 32)

class stones(behaviors):
    def __init__(self):
        super().__init__()
        self.sprite_px = 32
        self.x = randint(170, 1410)
        self.y = randint(160, 865)
        self.image = img_exact('stone', current_dir)
        self.rect = p.Rect(self.x, self.y, 32, 32)

class Intail_generation(behaviors):
    def __init__(self,biome):
        super().__init__()
        
        
        if biome == 'forest':
            rnd_trees = randint(10,20)
            rnd_stones = randint(4,10)
        elif biome == 'water':
            rnd_trees = 0
            rnd_stones = 0
        elif biome == 'stone':
            rnd_trees = randint(0,5)
            rnd_stones = randint(10,20)
        elif biome == 'sand':
            rnd_trees = randint(0,3)
            rnd_stones = randint(10,20)
        
        self.trees_list = []
        self.stones_list = []

        for _ in range(rnd_trees):
            self.trees_list.append(trees())
        for _ in range(rnd_stones):
            self.stones_list.append(stones())

        