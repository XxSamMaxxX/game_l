from controller.module.module import*
from scene.path import*

#obj

#display
FPS = 60
WIDTH, HEIGHT = 1920, 1080

screen = p.display.set_caption('Настолка')
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE)
clock = p.time.Clock()

#сolors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)