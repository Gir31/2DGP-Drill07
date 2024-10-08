from pico2d import *
import random

# Game object class here
class Grass:
    # 생성자 함수 : 객체의 초기 상태 설정
    def __init__(self):
        self.image = load_image('grass.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(1, 800), 599
        self.speed = random.randint(2, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        self.y -= self.speed
        self.stop()

    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        if self.y <= 60: self.speed = 0

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(1, 800), 599
        self.speed = random.randint(2, 10)
        self.image = load_image('ball41x41.png')

    def update(self):
        self.y -= self.speed
        self.stop()

    def draw(self):
        self.image.draw(self.x, self.y)

    def stop(self):
        if self.y <= 60: self.speed = 0

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    global grass
    global team
    global world
    global smallball
    global bigball

    running = True
    world = []

    grass = Grass() # 잔디 생성
    world.append(grass)

    team = [Boy() for i in range(11)] # 소년 생성
    world += team

    small = random.randint(1, 20)

    smallball = [SmallBall() for i in range(small)]
    bigball = [BigBall() for i in range(20 - small)]
    world += smallball
    world += bigball

running = True

def update_world():
    # 객체의 상태를 업데이트
    for o in world:
        o.update()
    pass

def render_world():
    clear_canvas()
    grass.draw()
    for o in world:
       o.draw()
    update_canvas()

open_canvas()

# initialization code
reset_world()

# game main loop code

while running:
    handle_events()
    update_world() # 상호작용을 시뮬레이션
    render_world() # 그 결과를 보여준다
    delay(0.05)


# finalization code
close_canvas()
