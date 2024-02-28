import pgzrun
from pgzero.actor import Actor

# Hücrelerden oluşan oyun penceresi
hucre = Actor("sınır")
hucre.width = 50 # Hücrenin genişliği
hucre.height = 50 # Hücrenin yüksekliği
WIDTH = 5*hucre.width
HEIGHT = 5*hucre.height

TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

def draw():
    hucre.draw()

pgzrun.go()