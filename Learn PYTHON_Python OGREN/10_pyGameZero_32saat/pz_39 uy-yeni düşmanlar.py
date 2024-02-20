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

for i in range(5):# Düşmanlar 
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    dusman = Actor("düşman", (x, y))
    dusman.hiz = random.randint(2, 8)
    dusmanlar.append(dusman)

def draw():# Çizimler
    uzay.draw()
    gemi.draw()
    for i in range(len(dusmanlar)):# Düşmanlar
        dusmanlar[i].draw()
    
def on_mouse_move(pos):# Kontroller
    gemi.pos = pos

def yeni_dusman():# Yeni düşmanlar
    x = random.randint(0, 400)
    y = -50
    dusman = Actor("düşman", (x, y))
    dusman.hiz = random.randint(2, 8)
    dusmanlar.append(dusman)

def dusman_gemisi():# Düşman hareketleri
    for i in range(len(dusmanlar)):
        if dusmanlar[i].y < 650:
            dusmanlar[i].y = dusmanlar[i].y + dusmanlar[i].hiz
        else:
            dusmanlar.pop(i)
            yeni_dusman()
def update(dt):
    dusman_gemisi()
pgzrun.go()
