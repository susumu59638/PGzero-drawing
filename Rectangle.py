import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400
TITLE = "Rectangles!"

def draw():
    screen.clear()
    screen.fill("#001845")
    r = randint(10,245)
    g = randint(10,245)
    b = randint(5,255)

    width = WIDTH
    height = HEIGHT - 300

    for i in range(30):
        box = Rect((0,0),(width,height))
        box.center = (200,200)
        screen.draw.rect(box,(r,g,b))

        width = width - 10
        height = height + 10





pgzrun.go()