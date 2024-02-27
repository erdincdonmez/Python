import pgzrun
from pgzero.actor import Actor
WIDTH = 600
HEIGHT = 400
TITLE = "Hayvan Avcısı"
FPS = 30

hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))

puan = 0
tiklama = 1

def draw():
    arkaplan.draw()
    hayvan.draw()
    screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)
    bonus_1.draw()
    screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
    screen.draw.text("Ücret : 15 Puan", center=(450, 110), color="black", fontsize = 20)
    bonus_2.draw()
    screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
    screen.draw.text("Ücret : 200$", center=(450, 210), color="black", fontsize = 20)
    
def on_mouse_down(button, pos):
    global puan
    if button == mouse.LEFT:
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
pgzrun.go()
