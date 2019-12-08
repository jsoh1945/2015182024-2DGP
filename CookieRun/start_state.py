import game_framework
from pico2d import *
import title_state
import main_state


LEN = 800
WID = 600
name = "StartState"
startImage = None
startButton = None
gotoHelp = None
logo_time = 0.0
sound = None

def enter():
    global startImage, startButton, gotoHelp, sound
    startImage = load_image('..\\CookieRun\\image_source\\title.png')
    startButton = load_image('..\\CookieRun\\image_source\\GameStart_button.png')
    gotoHelp = load_image('..\\CookieRun\\image_source\\help.png')
    sound = load_music('Title.mp3')
    sound.set_volume(32)
    sound.repeat_play()
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
            elif event.x < 400+100 and event.x > 400-100 and event.y < 500+30 and event.y > 500-30:
                game_framework.change_state(main_state)
    pass


def pause(): pass


def resume(): pass




