import pgzrun

WIDTH, HEIGHT = 500, 450
TITLE = "TRIANGLES"

def triangle():
    screen.draw.line((200,200), (300,300),"orange")
    screen.draw.line((300,300), (200,300),"orange")
    screen.draw.line((200,300), (200,200),"orange")

def draw():
    screen.clear()
    screen.fill("#2f243a")
    triangle()


pgzrun.go()


