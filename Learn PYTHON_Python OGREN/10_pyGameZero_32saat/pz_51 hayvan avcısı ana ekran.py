# OYUN EKRANINI OLUŞTURMA
import pgzrun
from pgzero.actor import Actor
WIDTH = 600
HEIGHT = 400
TITLE = "Hayvan Avcısı"
FPS = 30
# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
# Değişkenler
puan = 0

def draw():
    arkaplan.draw()
    hayvan.draw()
    screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)

pgzrun.go()
