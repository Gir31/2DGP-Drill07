from pico2d import *
import random

class Ball:
    def __init__(self):
        open_canvas()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():

    running = True

def update_world():
    # 객체의 상태를 업데이트
    pass

def render_world():
    clear_canvas()

    update_canvas()
# initialization code
reset_world()

# game main loop code

while running:
    handle_events()
    update_world()  # 상호작용을 시뮬레이션
    render_world()  # 그 결과를 보여준다
    delay(0.05)

# finalization code
close_canvas()