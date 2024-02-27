import pgzrun
from pgzero.actor import Actor
from pgzero.clock import schedule_interval
WIDTH = 600
HEIGHT = 400
TITLE = "Hayvan Avcısı"
FPS = 30

hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
oyna = Actor("oyna", (300, 100))
puan = 0
tiklama = 1
mod = 'menü'
ucret_1 = 15
ucret_2 = 200
ucret_3 = 600

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
        screen.draw.text(str(ucret_1), center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(str(ucret_2), center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("Her 2 saniye için 50$", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(str(ucret_3), center=(450, 310), color="black", fontsize = 20)

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
    global ucret_1, ucret_2, ucret_3
    if button == mouse.LEFT and mod == "oyun":# Oyun Modu
        if hayvan.collidepoint(pos):# Hayvanın üzerinde tıklama
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
        elif bonus_1.collidepoint(pos):# bonus_1 butonu tıklandığında
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 *= 2
        elif bonus_2.collidepoint(pos):# bonus_2 butonu tıklandığında
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 2)
                puan -= ucret_2
                ucret_2 *= 2
        elif bonus_3.collidepoint(pos):# bonus_3 button tıklandığında
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 2)
                puan -= ucret_3
                ucret_3 *= 2
    elif mod == 'menü' and button == mouse.LEFT:# Menü Modu
        if oyna.collidepoint(pos):
            mod = 'oyun'

pgzrun.go()
