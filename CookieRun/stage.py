from pico2d import *
import game_framework
import time

class ParallexLayer:
    def __init__(self, imageName):
        self.image = load_image(imageName)
        self.w, self.h = 800, 600
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.frame = 0

    def draw(self):
        self.image.clip_draw_to_origin(self.x1, 0, self.w1, self.h, 0, 0)
        self.image.clip_draw_to_origin(self.x2, 0, self.w2, self.h, self.w1, 0)
    
    def update(self):
        self.frame += int(500 * game_framework.frame_time)
        self.x1 = self.frame % self.image.w
        self.w1 = self.image.w - self.x1
        self.x2 = 0
        self.w2 = self.cw - self.w1

class Stage:
    First, Second = 0, 1
    def __init__(self):
        self.Fstage = [
            ParallexLayer('..\\CookieRun\\image_source\\Stage_01.png')
            ]
        self.Sstage = [
            ParallexLayer('..\\CookieRun\\image_source\\Stage_02.png')
            ]
        self.state = self.First
        self.StartTime = time.time()
        self.StateTime = 0

        # 사운드
        self.stage_1_sound = load_music('Stage1.mp3')
        self.stage_1_sound.set_volume(50)
        self.stage_1_sound.repeat_play()

    def draw(self):
        if self.state == self.First:
            for l in self.Fstage: l.draw()
        elif self.state == self.Second:
            for l in self.Sstage: l.draw()

    def update(self):

        if self.StateTime < 66.5:
            self.StateTime = time.time() - self.StartTime

            if self.StateTime >= 66.5:
                self.state = self.Second
                self.stage_2_sound = load_music('Stage2.mp3')
                self.stage_2_sound.set_volume(50)
                self.stage_2_sound.repeat_play()


        if self.state == self.First:
            for l in self.Fstage: l.update()
        elif self.state == self.Second:
            for l in self.Sstage: l.update()
