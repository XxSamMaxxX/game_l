from controller.module.module import os, choice, p, randint, choices

def img_exact(name, current_dir):

    img_dir = os.path.join(current_dir, '..', 'img')
    img = p.image.load(os.path.join(img_dir, name +'.png'))

    return img


def img_any(name, current_dir, preset=True):
    img_dir = os.path.join(current_dir, '..', 'img', name)
    
    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(img_dir, filename)
            image_paths.append(image_path)
    
    if preset:
        elements = image_paths  
        num_elements = len(elements)
        probabilities = []

        if num_elements == 2:
            probabilities = [0.7, 0.3]
        elif num_elements == 3:
            probabilities = [0.6, 0.2, 0.1]
        elif num_elements == 4:
            probabilities = [0.5, 0.2, 0.15, 0.15]
        elif num_elements == 5:
            probabilities = [0.4, 0.2, 0.15, 0.15, 0.1]
        elif num_elements == 6:
            probabilities = [0.35, 0.2, 0.15, 0.15, 0.1, 0.05]
        else:
            selected_image_path = choice(image_paths)
            image = p.image.load(selected_image_path)
        selected_image_path = choices(elements, probabilities, k=1)[0]
        image = p.image.load(selected_image_path)
    else:
        selected_image_path = choice(image_paths)
        image = p.image.load(selected_image_path)

    return selected_image_path, image

def img_animation(name, current_dir,):
    img_dir = os.path.join(current_dir, '..', 'img',name)

    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(img_dir, filename)
            image_paths.append(image_path)

    images = []
    for image_path in image_paths:
        image = p.image.load(image_path)
        images.append(image)
    return images

def img_all(current_dir,):
    img_dir = os.path.join(current_dir, '..', 'img')

    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(img_dir, filename)
            image_paths.append(image_path)

    images = []
    for image_path in image_paths:
        image = p.image.load(image_path)
        images.append(image)
    return images

def img_all_folder(name, current_dir,):
    img_dir = os.path.join(current_dir, '..', 'img', name)

    image_paths = []
    for filename in os.listdir(img_dir):
        if filename.endswith('.png'):
            image_path = os.path.join(img_dir, filename)
            image_paths.append(image_path)

    images = []
    for image_path in image_paths:
        image = p.image.load(image_path)
        images.append(image)
    return images

