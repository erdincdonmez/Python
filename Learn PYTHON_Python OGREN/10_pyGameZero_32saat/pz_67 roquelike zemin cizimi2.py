import pgzrun
from pgzero.actor import Actor
# Hücrelerden oluşan oyun penceresi
hucre = Actor("sınır")
hucre.width = 50 # Hücrenin genişliği
hucre.height = 50 # Hücrenin yüksekliği
WIDTH = 7 * hucre.width
HEIGHT = 7 * hucre.height

TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
haritam = [[0, 0, 0, 0, 0, 0, 0], 
           [0, 1, 2, 1, 3, 1, 0], 
           [0, 1, 1, 2, 1, 1, 0], 
           [0, 3, 2, 1, 1, 3, 0], 
           [0, 1, 1, 1, 3, 1, 0], 
           [0, 1, 3, 1, 1, 2, 0], 
           [0, 0, 0, 0, 0, 0, 0]]
          
def draw():
    hucre.draw()

pgzrun.go()