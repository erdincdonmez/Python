import pgzrun
from pgzero.actor import Actor

WIDTH = 300 # Pencere genişliği
HEIGHT = 300 # Pencere yüksekliği

TITLE = "Dişli" # Oyun için bir isim
FPS = 30 # Saniyedeki kare sayısı

#Karakterinizi oluşturacağınız kodlar
disli = Actor('dişli', (150, 150))

def draw():
    screen.fill('white')
    disli.draw()

def update(dt):
    disli.angle = disli.angle - 10

pgzrun.go()

