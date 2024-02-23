import pgzrun
from pgzero.actor import Actor

WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Sol tuş kullanımı" # Pencere Adı
FPS = 30 # Saniyedeki Kare Sayısı
sayac = 0

def draw():
    # screen.fill("(32, 191, 107)")
    screen.fill("olive")
    screen.draw.text(str(sayac), center=(150, 150), color="white", fontsize = 96)
    
def on_mouse_down(button, pos):
    global sayac
    if button == mouse.LEFT:
        sayac = sayac + 1

pgzrun.go()
