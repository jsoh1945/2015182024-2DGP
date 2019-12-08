import game_framework
import start_state
from pico2d import *

LEN = 800
WID = 600
name = "TitleState"
helpImage = None
titleImage = None
backImage = None
sound = None
def enter():
    global helpImage, titleImage, backImage, sound
    helpImage = load_image('..\\CookieRun\\image_source\\key.png')
    titleImage = load_image ('..\\CookieRun\\image_source\\title.png')
    backImage = load_image('..\\CookieRun\\image_source\\back.png')
    pass


def exit():
    global helpImage, titleImage, backImage
    del(helpImage)
    del(titleImage)
    del(backImage)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            if event.x < 650+100 and event.x > 650-100 and event.y < 500+50 and event.y > 500-50:
                game_framework.change_state(start_state)
    pass


def draw():
    clear_canvas()
    titleImage.draw(LEN//2,WID//2)
    helpImage.draw(400,300)
    backImage.draw(650,100)
    update_canvas()
    pass


def update():
    pass


def pause():
    pass


def resume():
    pass






