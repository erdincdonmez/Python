import pgzrun
from pgzero.actor import Actor

WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Kontrol Örneği" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli = Actor('uzaylı', (150, 150))
arkaplan = Actor("uzaylı_arkaplan")

def draw():
    arkaplan.draw()
    uzayli.draw()
   
def update(dt):
    if keyboard.left:
        # Sol ok tuşuna bastığınızda ne oluyor?
        uzayli.x = uzayli.x - 5

pgzrun.go() 



