from map.tail.script.tail import*
from building.areas.script.building_area import*
count_tails = 826
biom_generate(count_tails)

#obj
start = time.time()
tail = [tails() for _ in range(count_tails)]
end = time.time()
print(end - start)
def save_data():
    data = []
    for t in tail:
        tail_data = {
            "x": t.x,
            "y": t.y,
            "image": t.full_image_path,
            "wood": t.wood,
            "iron": t.iron,
            "wheat": t.wheat,
            "metal": t.metal
        }
        data.append(tail_data)
    with open('data.json', 'w') as file:
        json.dump(data, file)



#display
FPS = 60
WIDTH, HEIGHT = 1920, 1080

screen = p.display.set_caption('Настолка')
screen = p.display.set_mode((WIDTH, HEIGHT), p.RESIZABLE)
clock = p.time.Clock()

#сolors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)