class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.center_x = width 
        self.center_y = height 
        self.scale = 1.0  # Начальный масштаб

    def get_scale(self):
        return self.scale

    def get_x(self):
        return self.center_x

    def get_y(self):
        return self.center_y

    def scale_plus(self):
        new_scale = self.scale + 0.1
        if 1.0 <= new_scale <= 1.5:
            self.scale = new_scale

    def scale_minus(self):
        new_scale = self.scale - 0.1
        if 1.0 <= new_scale <= 1.5:
            self.scale = new_scale
    def move_left(self):
        self.center_x -= 100

    def move_right(self):
        self.center_x += 100

    def move_up(self):
        self.center_y -= 100

    def move_down(self):
        self.center_y += 100

    def is_point_visible(self, x, y):
        return -100 <= x < 1920 and -100 <= y < 1080