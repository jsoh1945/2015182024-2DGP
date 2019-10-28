import game_framework
from pico2d import *
import title_state

LEN = 800
WID = 600
name = "StartState"
startImage = None
startButton = None
gotoHelp = None
logo_time = 0.0


def enter():
    global startImage, startButton, gotoHelp
    startImage = load_image('..\\CookieRun\\image_source\\title.png')
    startButton = load_image('..\\CookieRun\\image_source\\GameStart_button.png')
    gotoHelp = load_image('..\\CookieRun\\image_source\\help.png')

    pass


def exit():
    global startButton, startImage, gotoHelp
    del(startImage)
    del(startButton)
    del(gotoHelp)
    pass


def update():
    pass


def draw():
    global startImage, startButton
    clear_canvas()
    startImage.draw(LEN//2,WID//2)
    startButton.draw(400,100)
    gotoHelp.draw(650,500)
    update_canvas()

    pass




def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEBUTTONDOWN:
            print(event.x)
            print(event.y)
            if event.x < 650+125 and event.x > 650-125 and event.y < 100+50 and event.y > 100-50:
                game_framework.change_state(title_state)
    pass


def pause(): pass


def resume(): pass




