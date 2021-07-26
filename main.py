from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d

app = Ursina()

camera.orthographic = True
camera.fov = 30


background = Entity(
    model='cube',
    texture='background.png',
    scale=(40, 28, 1),
    z=2
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(80, 28, 1),
    z=2
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(120, 28, 1),
    z=2
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(160, 28, 1),
    z=2
)

background = Entity(
    model='cube',
    texture='background.png',
    scale=(200, 28, 1),
    z=2
)



ground = Entity(
    model='cube',
    color=color.rgb(50, 180, 50),
    z=0.1,
    y=-8,
    scale=(200, 5, 10),
    collider='box'
)

wall = Entity(
    model='cube',
    color=color.rgb(50, 180, 50),
    collider='box',
    position=(-3, 0),
    scale=(5, 1)
)



for i in range(13):
    don = Entity(
        model='cube',
        texture='don.png',
        color=color.white,
        collider='box',
        position=(15, -5),
        scale=1
    )



player = PlatformerController2d(
    position=(-20, -5),
    texture='boshy.png',
    color=color.white,
    scale=1,
    max_jumps=2.5
)

spikes = []
# 반복을 우리는 13번을 한다. 근데 겹쳐서 스파이크가 13개가 나오지 않는다. 그러면 우리는 어떻게 이걸 겹치지 않고 해결할 수 있을까? 
# random.randint가 스파이크의 X축 위치를 결정하는 숫자이다.
# 
for i in range(13):
    spike = Entity(
        model='cube',
        texture='spike.png',
        color=color.white,
        collider='box',
        position=(random.randint(-15, 15), -5),
        scale=1
    )

    spikes.append(spike)

def update():
    hit_info = player.intersects()

    if hit_info.hit:
        if hit_info.entity in spikes:
            player.position = (-20, -5)



app.run()
