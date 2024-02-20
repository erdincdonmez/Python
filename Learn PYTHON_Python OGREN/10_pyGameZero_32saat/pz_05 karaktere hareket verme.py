import pgzrun
from pgzero.actor import Actor

WIDTH = 600  
HEIGHT = 300  

TITLE = "Oyun Adı" 
FPS = 30  

uzayli = Actor('uzayli', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")

def draw():
    arkaplan.draw()
    uzayli.draw()

def update(dt): # Bir saniyede FPS kadar çalıştır.
    uzayli.x = uzayli.x + 5
    uzayli.angle = uzayli.angle + 3

pgzrun.go()