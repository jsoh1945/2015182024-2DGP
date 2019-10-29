
from pico2d import *
import random

class Jelly:
    image = None
    MOVING, COLLIDING = range(2)
    def __init__(self):
        if self.image == None:
            self.image = load_image('..\\CookieRun\\image_source\\Item_Jelly.png')
            self.x = 820
            self.y = 270 + random.randint(0, 200)
            self.state = self.MOVING

    def update(self):
        if self.state == self.MOVING:
            self.x -= 10
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        pass
