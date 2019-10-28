import random
import json
import os

from pico2d import *
from character import Cookie

import game_framework
import start_state



name = "MainState"


class Grass:
    def __init__(self):
        self.image = load_image('..\\CookieRun\\image_source\\Ground_01.png')

    def draw(self):
        self.image.draw(400, 400)


character = None
grass = None

def enter():
    global grass, character
    character = Cookie()
    grass = Grass()
    pass


def exit():
    global grass, character
    del(grass)
    del(character)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    pass


def update():
    pass


def draw():
    global character
    clear_canvas()
    character.draw()
    grass.draw()
    character.update()
    update_canvas()
    delay(0.1)
    pass





