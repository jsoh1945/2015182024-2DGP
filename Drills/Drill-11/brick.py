from pico2d import *

class brick:
    def __init__(self):
        self.x, self.y = 1600 // 2, 600 // 2
        self.dir = 1
        self.image = load_image('brick180x40.png')

    def update(self):
        if self.x >= 1400 and self.dir > 0:
            self.dir = -1
        elif self.x <= 100 and self.dir < 0:
            self.dir = 1
        self.x += self.dir
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())


    def get_bb(self):
        return self.x - 90, self.y -20, self.x+90, self.y+ 20
