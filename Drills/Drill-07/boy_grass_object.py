from pico2d import *
import random

class Boy:
    def __init__(self):
        self.x = random.randint(100,700)
        self.y = 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame +1) % 8
        self.x += 5

    def draw(self):

        self.image.clip_draw(self.frame*100,0,100,100,self.x, self.y)

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class BBall:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(50,750)
        self.y = 599
        self.speed = random.randint(5,10)

    def draw(self):
        self.image.draw(self.x,self.y)

    def update(self):
        if self.y <= 80:
            pass
        else:
            self.y -= self.speed


class SBall:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(50,750)
        self.y = 599
        self.speed = random.randint(5,10)

    def draw(self):
        self.image.draw(self.x,self.y)


    def update(self):
        if self.y <= 80:
            pass
        else:
            self.y -= self.speed


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

W = 800
H = 600
open_canvas(W,H)
grass = Grass()

#boy = Boy()

team = [Boy() for i in range(11)]
Num_Small = random.randint(0,20)
Num_Big = 20 - Num_Small
Sballs = [BBall() for i in range(Num_Small)]
Bballs = [SBall() for j in range(Num_Big)]
running = True

while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for Sball in Sballs:
        Sball.draw()
    for Sball in Sballs:
        Sball.update()
    for Bball in Bballs:
        Bball.draw()
    for Bball in Bballs:
        Bball.update()

    for boy in team:
        boy.draw()
    for boy in team:
        boy.update()
    update_canvas()
    delay(0.05)

# game main loop code
close_canvas()
# finalization code