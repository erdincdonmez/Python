#pgzero
import pgzrun



WIDTH = 600 # Pencere Genişliği
HEIGHT = 500 # Pencere Yüksekliği

TITLE = "Oyun Adı" # Oyununuz için bir isim belirleyebilirsiniz
FPS = 30 # Saniyedeki kare sayısı

def draw():
    screen.clear()
    screen.draw.circle((400, 300), 30, 'white')

pgzrun.go()
