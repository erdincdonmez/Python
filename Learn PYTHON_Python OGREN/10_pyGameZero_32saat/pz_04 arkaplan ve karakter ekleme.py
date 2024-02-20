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

pgzrun.go()