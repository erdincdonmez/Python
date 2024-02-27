# PUAN ARTIRALIM
import pgzrun
from pgzero.actor import Actor
WIDTH = 600
HEIGHT = 400
TITLE = "Hayvan Avcısı"
FPS = 30
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
puan = 0
tiklama = 1
def draw():
    arkaplan.draw()
    hayvan.draw()
    screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)

def on_mouse_down(button, pos): # tıklama durumu
    global puan
    if button == mouse.LEFT:
        # Hayvanın üzerinde tıklama var mı
        if hayvan.collidepoint(pos): 
            puan += tiklama # += ekle, -=, *=, /=
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
pgzrun.go()
