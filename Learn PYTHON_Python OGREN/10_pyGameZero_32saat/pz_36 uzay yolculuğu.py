import pgzrun
from pgzero.actor import Actor

WIDTH = 600
HEIGHT = 450

TITLE = "Uzay Yolculuğu"
FPS = 30

# Nesneler ve Değişkenler
gemi = Actor("gemi", (300, 400))
uzay = Actor("uzay")

# Karakterlerin çizimi
def draw():
    uzay.draw()
    gemi.draw()
               
pgzrun.go()
