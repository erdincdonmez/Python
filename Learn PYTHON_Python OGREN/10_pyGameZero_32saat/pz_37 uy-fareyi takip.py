import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 450
TITLE = "Uzay Yolculuğu"
FPS = 30

gemi = Actor("gemi", (300, 400))
uzay = Actor("uzay")

def draw():# Çizimler
    uzay.draw()
    gemi.draw()
    
def on_mouse_move(pos):# Kontroller
    gemi.pos = pos
               
pgzrun.go()
