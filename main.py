import pgzrun
from random import randint
from time import time

WIDTH = 800
HEIGHT = 600

sunflowers = []
lines = []
next_sunflower = 0

start_time = 0
total_time = 0
end_time = 0

number_of_sunflower = 8

def create_sunflowers():
    global start_time 
    for count in range(0, number_of_sunflower):
        sunflower = Actor("sunflower")
        sunflower.pos = randint(40, WIDTH-40), randint(40, HEIGHT-40)
        sunflowers.append(sunflower)
    start_time = time()


def draw():
    global total_time

    screen.blit("background", (0,0))
    number = 1
    for sunflower in sunflowers:
        screen.draw.text(str(number), (sunflower.pos[0], sunflower.pos[1]+20))
        sunflower.draw()
        number = number + 1
    
    for line in lines:
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_sunflower < number_of_sunflower:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=30)


def update():
    pass


def on_mouse_down(pos):
    global next_sunflower, lines

    if next_sunflower < number_of_sunflower:
        if sunflowers[next_sunflower].collidepoint(pos):
            if next_sunflower:
                lines.append((sunflowers[next_sunflower-1].pos, sunflowers[next_sunflower].pos))
            next_sunflower = next_sunflower + 1
        else:
            lines = []
            next_sunflower = 0


create_sunflowers()

pgzrun.go()