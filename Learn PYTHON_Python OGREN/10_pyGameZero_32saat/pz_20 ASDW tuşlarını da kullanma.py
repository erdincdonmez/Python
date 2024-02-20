import pgzrun
from pgzero.actor import Actor

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği

TITLE = "Uzaylı Yarışı" # Oyun Adı
FPS = 30 # Saniyedeki Kare Sayısı

uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))
new_image = 'uzaylı' # Geçerli olan resimi takip edecek

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    
def update(dt):
    global new_image 

    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else: kutu.x = WIDTH + 20
        
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x = uzayli.x - 5

        if new_image != 'uzaylı_sol':
            uzayli.image = 'uzaylı_sol'
            new_image = 'uzaylı_sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if new_image != 'uzaylı_sağ':
            uzayli.image = 'uzaylı_sağ'
            new_image = 'uzaylı_sağ'
    else:
        uzayli.image = 'uzaylı'
        new_image = 'uzaylı'

def on_key_down(key): # Zıplama
    
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

pgzrun.go() 



