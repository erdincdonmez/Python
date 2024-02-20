import pgzrun
from pgzero.actor import Actor

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Koşusu" # Oyununuzun Adı
FPS = 30 # Saniyedeki Kare Sayısı

#Karakterlerinizi oluşturacak olan kodları buraya yazınız
uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("arkaplan")
kutu = Actor('kutu', (550, 265))

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()

pgzrun.go() 