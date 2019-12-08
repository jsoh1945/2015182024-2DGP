import random
import game_world
from pico2d import *
import game_framework

from character import Cookie
from stage import Stage
from ground import Ground
from hp import HP
from potion import Potion
from jelly import Jelly
#함정들
from djtrap import djTrap
from jtrap import jTrap
from strap import sTrap
#스코어
import Score_state
import score

import start_state



name = "MainState"


class Background:
    def __init__(self):
        self.image = load_image('..\\CookieRun\\image_source\\Stage_01.png')

    def draw(self):
        self.image.draw(400,300)


def collides(a, b):
    if not hasattr(a, 'get_bb'): return False
    if not hasattr(b, 'get_bb'): return False

    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False
    return True

#ground, character, stage, hp = None
#scoreLabel, Label = None
#jelly_sound, collide_sound, item_eat = None

def enter():
    global ground, character, stage,hp
    global scoreLabel, Label
    global jelly_sound, collide_sound, item_eat

    character = Cookie()
    stage = Stage()
    ground = Ground()
    hp = HP()

    game_world.add_object(character, 1)
    game_world.add_object(stage, 0)
    game_world.add_object(ground, 0)
    game_world.add_object(hp, 0)

    label = score.Label("Score: ", 50, get_canvas_height() -50,45,0)
    label.color = (255,255,255)
    score.labels.append(label)
    scoreLabel = label

    jelly_sound = load_wav('jelly.wav')
    jelly_sound.set_volume(32)
    item_eat = load_wav('item.wav')
    item_eat.set_volume(32)
    collide_sound = load_wav('collide.wav')
    collide_sound.set_volume(50)

def exit():
    game_world.clear()
    Score_state.scoretemp = character.score


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_0):
            hp.HP_count += 500
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            pass
        else:
            character.handle_events(event)
    pass


def update():
    create = random.randint(0, 100)
    TrapPattern = random.randint(0, 3)

    # 오브젝트 생성
    if character.item_count > 0.01:
        jelly = Jelly()  # 젤리 (점수)
        game_world.add_object(jelly, 0)
        # 0.01초마다 5% 확률로 포션 생성
        if create < 5:
            potion = Potion()
            game_world.add_object(potion, 0)
        character.item_count = 0

    if character.count >= 1.0:
        if TrapPattern == 0:
            jump_trap = jTrap()  # 1단 점프 함정
            game_world.add_object(jump_trap, 0)
            character.count = 0
        elif TrapPattern == 1:
            double_jump_trap = djTrap()  # 2단 점프 함정
            game_world.add_object(double_jump_trap, 0)
            character.count = 0
        elif TrapPattern == 2:
            strap = sTrap()  # 슬라이드 함정
            game_world.add_object(strap, 0)
            character.count = 0

    # 게임월드 업데이트
    for game_object in game_world.all_objects():
        game_object.update()
    # 충돌처리
    for obj in game_world.all_objects():
        if isinstance(obj, Jelly) and hp.HP_count >= 0:
            if collides(character, obj):
                character.score += 5
                jelly_sound.play()
                game_world.remove_object(obj)
        if isinstance(obj, Potion):
            if collides(character, obj) and hp.HP_count >= 0:
                hp.HP_count += 30
                item_eat.play()
                game_world.remove_object(obj)
        # 함정
        if isinstance(obj, jTrap):
            if collides(character, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                character.fps = 0
                character.state = character.COLLIDE
                hp.HP_count -= 50
        if isinstance(obj, djTrap):
            if collides(character, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                character.fps = 0
                character.state = character.COLLIDE
                hp.HP_count -= 50
        if isinstance(obj, sTrap):
            if collides(character, obj) and hp.HP_count >= 0:
                game_world.remove_object(obj)
                collide_sound.play()
                character.fps = 0
                character.state = character.COLLIDE
                hp.HP_count -= 50

        update_score()

        if hp.HP_count <= 0:
            character.x -= 10 * game_framework.frame_time
            if character.x <= -500:
                game_framework.change_state(Score_state)


def update_score():
    global scoreLabel
    str = "Score: {:0.0f}".format(character.score)
    scoreLabel.text = str

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    score.draw()
    update_canvas()



