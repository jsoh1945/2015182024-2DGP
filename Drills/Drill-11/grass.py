from pico2d import *

class Grass:
    def __init__(self):
        self.x, self.y = 400, 30
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(1200, 30)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return 0,0, 1600,50
