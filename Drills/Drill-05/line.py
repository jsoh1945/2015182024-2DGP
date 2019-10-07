from pico2d import *
import random

KPU_HEIGHT, KPU_WIDTH = 720, 1280




def draw_line(p1, p2):
    for i in range(0, 100 + 1, 5):
        t = i / 100
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    pass


def handle_events():
    global running, moving
    global Mx, My
    global Cx, Cy
    global desX, desY
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            Mx, My = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            moving = True
            desX, desY = event.x - 25, 720 - event.y + 50
            #draw_line((Cx, Cy), (event.x - 25, 720 - event.y + 50))
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



open_canvas(KPU_WIDTH, KPU_HEIGHT)

kpu_ground = load_image("KPU_GROUND.png")
character = load_image("animation_sheet.png")
cursor = load_image("hand_arrow.png")

running = True
moving = False
Cx, Cy = KPU_WIDTH // 2, KPU_HEIGHT // 2
desX, desY = 0, 0
CxO, CyO = KPU_WIDTH // 2, KPU_HEIGHT // 2
Mx, My = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()


while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    character.clip_draw(frame * 100, 100 * 1, 100, 100, Cx, Cy)
    if moving:
        draw_line((Cx,Cy),(desX,desY))

    cursor.draw(Mx, My)
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()
    delay(0.05)

close_canvas()
