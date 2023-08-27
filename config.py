from map.tail.script.tail import*
from building.areas.script.building_area import*
count_tails = 826
biom_generate(count_tails)

#obj
start = time.time()
tail = [tails() for _ in range(count_tails)]
end = time.time()
print(end - start)

#display
FPS = 60
WIDTH, HEIGHT = 1920, 1080

screen = p.display.set_caption('Настолка')
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE)
clock = p.time.Clock()

#сolors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)