import pgzrun
from pygame.transform import scale
from pgzero.actor import Actor

WIDTH = 600  
HEIGHT = 300 
TITLE = "Döndürme" 
FPS = 30 

disli = Actor('dişli', (150, 150))
bomb1 = Actor('bomb4', (450, 0))
bomb2 = Actor('bomb4', (250, 0))
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
bomb1._surf = scale(bomb1._surf, (50, 50))    

def draw():
    arkaplan.draw()
    uzayli.draw()
    disli.draw()
    bomb1.draw()
    bomb2.draw()

def update(dt):
    disli.angle = disli.angle - 10
    uzayli.x = uzayli.x + 5
    uzayli.angle = uzayli.angle + 3
    bomb1.y += 1
    if bomb1.y >= HEIGHT : bomb1.y = 0

pgzrun.go() 