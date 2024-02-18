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

durum = "zipladi"

def update(dt):
    global durum
    if keyboard.left:
        uzayli.x = uzayli.x - 5
    if keyboard.right:
        uzayli.x = uzayli.x + 5
    if keyboard.up:
        uzayli.y = uzayli.y - 5
    if keyboard.down:
        uzayli.y = uzayli.y + 5
    if keyboard.space:
        if durum == "zipladi": 
            uzayli.y = uzayli.y + 30
            durum = "yerde"
        else: 
            uzayli.y = uzayli.y - 30
            durum = "zipladi"

pgzrun.go() 



