import game_framework
from pico2d import *


class Cookie:
    Image = None
    RUNNING, JUMPING, COLLIDING, SLIDING = range(4)
    def __init__(self):
        self.x = 150
        self.y = 265
        self.state = self.RUNNING
        self.cookie_running = load_image('..\\CookieRun\\image_source\\Cookie_Run_State.png')
        self.cookie_colliding = load_image('..\\CookieRun\\image_source\\cookie_run_collid.png')
        self.frame = 0


    def update(self):
        if self.state == self.RUNNING:
            if self.frame > 3:
                self.frame = 0
            self.frame = (self.frame + 1) % 3
        elif self.state == self.JUMPING:
            self.frame = (self.frame + 1) % 6

        elif self.state == self.SLIDING:
            if self.frame > 2:
                self.frame = 0
            self.frame = (self.frame + 1) % 2

    def draw(self):
        if self.state == self.RUNNING:
            self.cookie_running.clip_draw(self.frame * 120,245,120,135,self.x,self.y)
        elif self.state == self.JUMPING:
            self.cookie_running.clip_draw(self.frame * 140, 80,140, 165,self.x,self.y)
        elif self.state == self.SLIDING:
            self.cookie_running.clip_draw(self.frame * 170,0,170,80, self.x,self.y)

    def handle_events(self,event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if self.state == self.RUNNING:
                self.state = self.SLIDING
                self.y = 220
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state == self.SLIDING:
                self.state = self.RUNNING
                self.y = 265

        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state == self.RUNNING:
                self.state = self.JUMPING
            elif self.state == self.SLIDING:
                self.state = self.JUMPING
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            if self.state == self.JUMPING:
                self.state = self.RUNNING


