import pgzrun
from pgzero.actor import Actor
from pgzero.clock import schedule_interval
WIDTH = 600
HEIGHT = 400

TITLE = "Hayvan Avcısı"
FPS = 30

# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
oyna = Actor("oyna", (300, 100))

# Değişkenler
puan = 0
tiklama = 1
mod = 'menü'

def draw():
    if mod == 'menü':
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(str(puan), center=(30, 20), color="white", fontsize = 36)
   
    elif mod == 'oyun':    
        arkaplan.draw()
        hayvan.draw()
        screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text("Ücret : 15$", center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text("Ücret : 200$", center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("Her 2 saniye için 50$", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text("Ücret : 600$", center=(450, 310), color="black", fontsize = 20)

def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def bonus_3_icin():
    global puan
    count += 50

def on_mouse_down(button, pos):
    global puan
    global mod
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
        # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            if puan >= 15:
                schedule_interval(bonus_1_icin, 2)
                puan -= 15
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            if puan >= 200:
                schedule_interval(bonus_2_icin, 2)
                puan -= 200
        # bonus_3 button tıklandığında
        elif bonus_3.collidepoint(pos):
            if puan >= 600:
                schedule_interval(bonus_3_icin, 2)
                puan -= 600
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
pgzrun.go()