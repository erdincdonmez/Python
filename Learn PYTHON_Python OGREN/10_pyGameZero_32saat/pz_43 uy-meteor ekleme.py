import pgzrun
from pgzero.actor import Actor
import random

WIDTH = 600
HEIGHT = 450
TITLE = "Uzay Yolculuğu"
FPS = 30
gemi = Actor("gemi", (300, 400))
uzay = Actor("uzay")
dusmanlar = []
meteorlar = []
mod = 'oyun'

for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)

for i in range(5):
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteorlar.append(meteor)

def draw():
    if mod == 'oyun':
        uzay.draw()
        for i in range(len(meteorlar)):
            meteorlar[i].draw()
        gemi.draw()
        for i in range(len(dusmanlar)):
            dusmanlar[i].draw()

    elif mod == 'son':
        uzay.draw()
        screen.draw.text("OYUN BİTTİ!", center = (300, 200), color = "white", fontsize = 36)
      
def on_mouse_move(pos):
    gemi.pos = pos

def yeni_dusman():
    x = random.randint(0, 400)
    y = -50
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)

def dusman_gemisi():
    for i in range(len(dusmanlar)):
        if dusmanlar[i].y < 650:
            dusmanlar[i].y = dusmanlar[i].y + dusmanlar[i].speed
        else:
            dusmanlar.pop(i)
            yeni_dusman()

def meteor_hareketi():
    for i in range(len(meteorlar)):
        if meteorlar[i].y < 450:
            meteorlar[i].y = meteorlar[i].y + meteorlar[i].speed
        else:
            meteorlar[i].x = random.randint(0, 600)
            meteorlar[i].y = -20
            meteorlar[i].speed = random.randint(2, 10)

def carpismalar():
    global mod
    for i in range(len(dusmanlar)):
        if gemi.colliderect(dusmanlar[i]):
            mod = 'son'

def update(dt):
    if mod == 'oyun':
        dusman_gemisi()
        carpismalar()
        meteor_hareketi()

pgzrun.go()
