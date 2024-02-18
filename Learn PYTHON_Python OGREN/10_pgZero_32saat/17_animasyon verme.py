import pgzrun
from pgzero.actor import Actor

WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Boşluk Tuşuna Basın" 
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli = Actor('uzaylı', (20, 20))
arkaplan = Actor("uzaylı_arkaplan")

def draw():
    arkaplan.draw()
    uzayli.draw()
    
def update(dt):
    if keyboard.space:
	    animate(uzayli, tween='linear', duration=1, x = 280, y = 280)

pgzrun.go() 



