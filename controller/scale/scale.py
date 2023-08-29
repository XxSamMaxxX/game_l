WIDTH, HEIGHT = 1920, 1080
scale = 1.0
center_x = WIDTH // 2
center_y = HEIGHT // 2


def get_scale():
    return scale
def get_x():
    return center_x
def get_y():
    return center_y

def scale_plus():
    global scale, center_x, center_y
    scale *= 1.1
def scale_minus():
    global scale, center_x, center_y
    scale /= 1.1

def camera_moving_left():
    global center_x
    center_x += 100
def camera_moving_right():
    global center_x
    center_x -= 100

def camera_up():
    global scale, center_x, center_y
    center_x -= 10
def camera_down():
    global scale, center_x, center_y
    center_x -= 10
