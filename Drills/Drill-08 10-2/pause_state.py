import game_framework
from pico2d import *
import main_state

name = "PauseState"

pause_image = None
character = None
grass = None
pause_time = 0.0

def enter():
    global pause_image, character, grass
    grass = load_image('grass.png')
    character = load_image('run_animation.png')
    pause_image = load_image('pause.png')
    pass


def exit():
    global pause_image, character, grass
    del(pause_image)
    del(character)
    del(grass)
    pass

def draw():
    clear_canvas()
    if pause_time > 150:
        pause_image.clip_draw(200, 200, 500, 500, 400, 300, 300, 300)
    character.clip_draw(main_state.boy.frame * 100, 0, 100, 100, main_state.boy.x, main_state.boy.y)
    grass.draw(400,30)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()

def update():
    global pause_time
    pause_time = (pause_time + 1) % 300

