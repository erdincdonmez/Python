import pgzrun
from pgzero.actor import Actor

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Title for the game window
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
kutu = Actor('kutu', (550, 265))

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()

def update(dt):
    # BKutunun Hareketi
    if kutu.x > - 20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20

pgzrun.go() 


