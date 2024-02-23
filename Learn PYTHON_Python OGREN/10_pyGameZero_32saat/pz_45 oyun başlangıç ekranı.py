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
gezegenler = [Actor("gezegen1", (random.randint(0, 600), -100)), Actor("gezegen2", (random.randint(0, 600), -100)), Actor("gezegen3", (random.randint(0, 600), -100))]
meteorlar = []
mod = 'menü'
gemi1 = Actor("gemi1", (100, 200))
gemi2 = Actor("gemi2", (300, 200))
gemi3 = Actor("gemi3", (500, 200))

for i in range(5):# Düşmanlar
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    dusman = Actor("düşman", (x, y))
    dusman.speed = random.randint(2, 8)
    dusmanlar.append(dusman)
    
for i in range(5):# Meteorlar
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteorlar.append(meteor)

def draw():# Oyun ekranı
    if mod == 'menü':# Başlangıç Menüsü
        uzay.draw()
        screen.draw.text('Bir Gemi Seçiniz', center = (300, 100), color = "white", fontsize = 36)
        gemi1.draw()
        gemi2.draw()
        gemi3.draw()
    if mod == 'oyun':# Oyun Modu
        uzay.draw()
        gezegenler[0].draw()
        for i in range(len(meteorlar)):# Meteorlar
            meteorlar[i].draw()
        gemi.draw()
        for i in range(len(dusmanlar)):# Düşmanlar
            dusmanlar[i].draw()
    elif mod == 'son':# Oyun Bitti ekranı
        uzay.draw()
        screen.draw.text("OYUN BİTTİ!", center = (300, 200), color = "white", fontsize = 36)

def on_mouse_move(pos):# Kontroller
    gemi.pos = pos

def yeni_dusman():# Yeni Düşman ekleme
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

def gezegen():# Gezegen Hareketleri
    if gezegenler[0].y < 550:
            gezegenler[0].y = gezegenler[0].y + 1
    else:
        gezegenler[0].y = -100
        gezegenler[0].x = random.randint(0, 600)
        birinci = gezegenler.pop(0)
        planets.append(birinci)

def meteorlar_hareket():# Meteor Hareketleri
    for i in range(len(meteorlar)):
        if meteorlar[i].y < 450:
            meteorlar[i].y = meteorlar[i].y + meteorlar[i].speed
        else:
            meteorlar[i].x = random.randint(0, 600)
            meteorlar[i].y = -20
            meteorlar[i].speed = random.randint(2, 10)

def carpismalar():# Çarpışmalar
    global mod
    for i in range(len(dusmanlar)):
        if gemi.colliderect(dusmanlar[i]):
            mod = 'son'

def update(dt):
    if mod == 'oyun':
        dusman_gemisi()
        carpismalar()
        gezegen()
        meteorlar_hareket()

pgzrun.go()
