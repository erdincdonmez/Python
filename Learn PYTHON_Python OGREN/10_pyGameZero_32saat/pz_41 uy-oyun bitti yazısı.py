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
mod = 'oyun'

for i in range(5):# Düşman listesi
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)

def draw():# Çizimler
    if mod == 'oyun':# Oyun modu
        uzay.draw()
        gemi.draw()
        for i in range(len(dusmanlar)):# Düşmanlar
            dusmanlar[i].draw()
    elif mod == 'son':# Oyun Sonu
        uzay.draw()
        screen.draw.text("OYUN BİTTİ!", center = (300, 200), color = "white", fontsize = 36)
    
def on_mouse_move(pos):# Kontroller
    gemi.pos = pos

def yeni_dusman():# Yeni düşmanlar
    x = random.randint(0, 400)
    y = -50
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)

def dusman_gemisi():# Düşman Hareketleri
    for i in range(len(dusmanlar)):
        if dusmanlar[i].y < 650:
            dusmanlar[i].y = dusmanlar[i].y + dusmanlar[i].speed
        else:
            dusmanlar.pop(i)
            yeni_dusman()

def carpismalar():# Çarpışmalar
    global mod
    for i in range(len(dusmanlar)):
        if gemi.colliderect(dusmanlar[i]):
            mod = 'son'

def update(dt):
    if mod == 'oyun':
        dusman_gemisi()
        carpismalar() 

pgzrun.go()
