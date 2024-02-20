import pgzrun
from pgzero.actor import Actor

WIDTH = 200 # Pencere Genişliği
HEIGHT = 200 # Pencere Yüksekliği

TITLE = "Kristaller" # Oyunumuzun İsmi
FPS = 30 # Saniyedeki Kare Sayısı

#Karakterlerinizi oluşturacağınız kodları buraya yazınız
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
    # Değişiklikleri ortaya çıkaracak kodları buraya yazınız
    mavi.x = mavi.x + 1
    mavi.y = mavi.y + 1
    kirmizi.x = kirmizi.x - 1
    kirmizi.y = kirmizi.y + 1  
    sari.x = sari.x - 1
    sari.y = sari.y - 1  
    yesil.x = yesil.x + 1
    yesil.y = yesil.y - 1  

pgzrun.go()

