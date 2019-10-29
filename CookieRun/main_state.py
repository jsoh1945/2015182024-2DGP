import random
import json
import os

from pico2d import *
from character import Cookie
import character

import game_framework
import start_state



name = "MainState"


class Ground:
    def __init__(self):
        self.image = load_image('..\\CookieRun\\image_source\\Ground_01.png')

    def draw(self):
        self.image.draw(400, 400)

class Background:
    def __init__(self):
        self.image = load_image('..\\CookieRun\\image_source\\Stage_01.png')

    def draw(self):
        self.image.draw(400,300)


character = None
ground = None
bg = None

def enter():
    global ground, character, bg
    character = Cookie()
    bg = Background()
    ground = Ground()
    pass


def exit():
    global ground, character,bg
    del(ground)
    del(character)
    del(bg)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            pass
        else:
            character.handle_events(event)
    pass


def update():
    pass


def draw():
    global character,ground,bg
    clear_canvas()
    bg.draw()
    character.draw()
    ground.draw()
    character.update()
    update_canvas()
    delay(0.05)
    pass





