import game_framework
from pico2d import *
import game_world
import random
import main_state


class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = random.randint(20,1280-20)
        self.y = random.randint(20,1024-20)
        self.size = 0
        self.big = False

    def draw(self):
        self.image.draw(self.x,self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x -10, self.y -10, self.x +10, self.y +10

    def update(self):
        pass

    def stop(self):
        pass

class BigBall(Ball):
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x = random.randint(20, 1280 - 20)
        self.y = random.randint(20, 1024 - 20)
        self.big = True

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

