import pgzrun
from random import randint

radius = 100
HEIGHT = 500
WIDTH = 500
TITLE = "Circles HW"

def draw():
    global radius
    screen.clear()
    screen.fill("#4A13C1")
    r = randint(5,168)
    g = randint(5,255)
    b = randint(5,30)

    for i in range(15):
        screen.draw.circle((250,250),radius,(r,g,b))

        radius = radius + 5


pgzrun.go()