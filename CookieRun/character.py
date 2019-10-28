import game_framework
from pico2d import *


class Cookie:

    def __init__(self):
        self.cookie_running = load_image('..\\CookieRun\\image_source\\Cookie_Run_State.png')
        self.frame = 0
        self.dir = 0


    def update(self):
        self.frame = (self.frame + 1) % 3

    def draw(self):
        self.cookie_running.clip_draw(self.frame * 120,245,120,135,150,265)

