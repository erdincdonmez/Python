import pgzrun
from pgzero.actor import Actor

WIDTH = 200 # Pencere Genişliği
HEIGHT = 200 # Pencere Yüksekliği

TITLE = "Kristaller" # Oyunumuzun İsmi

mavi = Actor('mavi', (20, 20))
kirmizi = Actor('kırmızı', (180, 20))
sari = Actor('sarı', (180, 180))
yesil = Actor('yeşil', (20, 180))

def draw():
    screen.fill('white')
    mavi.draw()
    kirmizi.draw()
    sari.draw()
    yesil.draw()

def update(dt):
    mavi.x = mavi.x + 1
    mavi.y = mavi.y + 1
    kirmizi.x = kirmizi.x - 1
    kirmizi.y = kirmizi.y + 1  
    sari.x = sari.x - 1
    sari.y = sari.y - 1  
    yesil.x = yesil.x + 1
    yesil.y = yesil.y - 1  
    if mavi.x > HEIGHT: mavi.x=0
    if mavi.y > WIDTH: mavi.y=0
    # Animasyonun devamlı olması için kalan kodları tamamla.

pgzrun.go() 