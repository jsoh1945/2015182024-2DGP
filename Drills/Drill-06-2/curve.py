from pico2d import *
import random

def drawPoints(p1,p2,p3,p4):
    global prevX, prevY

    for i in range(0,100,2):
        t = i / 100
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (
                    -3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2
        characterMove((x,y))

def characterMove(point):
    global frame
    global prevX, prevY
    clear_canvas()
    bg.draw(KPU_WIDTH // 2 ,KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, point[0], point[1])
    frame = (frame + 1) % 8
    update_canvas()
    delay(0.05)

def setRanPoint():
    x = random.randint(50,KPU_WIDTH-50)
    y = random.randint(50,KPU_HEIGHT-50)
    return x,y

def draw10Points(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10):
    drawPoints(p1,p2,p3,p4)
    drawPoints(p2, p3, p4, p5)
    drawPoints(p3, p4, p5, p6)
    drawPoints(p4, p5, p6, p7)
    drawPoints(p5, p6, p7, p8)
    drawPoints(p6, p7, p8, p9)
    drawPoints(p7, p8, p9, p10)

KPU_WIDTH, KPU_HEIGHT = 1280, 720
open_canvas(KPU_WIDTH,KPU_HEIGHT)
bg = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
prevX, prevY = 0, 0

points = [setRanPoint(), setRanPoint(),setRanPoint(), setRanPoint(),setRanPoint(),
          setRanPoint(),setRanPoint(), setRanPoint(),setRanPoint(), setRanPoint()]

size = len(points)
frame = 0

while True:
    draw10Points(points[0],points[1],points[2],points[3],points[4],points[5],points[6],points[7],points[8],points[9])


