from controller.module.module import*
from map.tail.script.tail import*

save_path = os.path.join('save', 'saved', 'data.json')

def save_save_data():
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
        
    with open(save_path, 'w') as file:
        json.dump(data, file)

def save_loaded_data():
    with open(save_path, 'r') as file:
        data = json.load(file)
        loaded_tails = []  

        for tail_data in data:
            new_tail = tails(1, tail_data["x"], tail_data["y"], tail_data["image"])                      
            new_tail.wood = tail_data["wood"]
            new_tail.iron = tail_data["iron"]
            new_tail.wheat = tail_data["wheat"]
            new_tail.metal = tail_data["metal"]

            loaded_tails.append(new_tail) 

        return loaded_tails
        
