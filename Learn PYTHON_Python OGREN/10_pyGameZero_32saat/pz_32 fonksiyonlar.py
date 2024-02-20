import pgzrun
from pgzero.actor import Actor
WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği
TITLE = "Düman Hareketi İçin Fonksiyon" 
FPS = 30 # Saniyedeki Kare Sayısı

robot = Actor('atari_ayakta', (50, 240))
arkaplan = Actor("atari_arkaplan")
dusman = Actor('atari_sarı', (250, 270))

def draw():
    arkaplan.draw()
    robot.draw()
    dusman.draw()
    
def dusmanlar(): # Düşman Hareketi
    if dusman.x > -20:
        dusman.x = dusman.x - 10
        dusman.angle = dusman.angle + 10
    else:
        dusman.x = WIDTH + 20

def update(dt):
    dusmanlar() # Fonksiyonun Çağrılması
    if keyboard.left and robot.x > 20:
        robot.x = robot.x - 5

    elif keyboard.right and robot.x < 280:
        robot.x = robot.x + 5

pgzrun.go()

