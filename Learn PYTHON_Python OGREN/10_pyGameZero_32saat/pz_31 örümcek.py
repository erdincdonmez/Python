import pgzrun
from pgzero.actor import Actor
from keyboard import is_pressed
WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği
TITLE = "Örümcek" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
orumcek = Actor('örümcek', (150, 150))
engel1 = Actor('örümcek_engel', (100, 250))
engel2 = Actor('örümcek_engel', (30, 30))
engel3 = Actor('örümcek_engel', (270, 120))
arkaplan = Actor("örümcek_arkaplan")
carpma = 0

def draw():
    arkaplan.draw()
    orumcek.draw()
    engel1.draw()
    engel2.draw()
    engel3.draw()
    if carpma == 1: screen.draw.text('Engele çarptınız', pos=(30, 150), color= "white", fontsize = 24)
    elif carpma == 2: screen.draw.text('Duvara çarptınız', pos=(30, 150), color= "white", fontsize = 24)
       
def update(dt):
    global carpma
    if keyboard.left and orumcek.x > 20: orumcek.x -= 5
    elif keyboard.right and orumcek.x < 280: orumcek.x += 5
    elif keyboard.up and orumcek.y > 20: orumcek.y -= 5
    elif keyboard.down and orumcek.y < 280: orumcek.y += 5
 
    if orumcek.colliderect(engel1) or orumcek.colliderect(engel2) or orumcek.colliderect(engel3): carpma = 1
    elif orumcek.x >= 280 or orumcek.x <= 20 or orumcek.y <= 20 or orumcek.y >= 280: carpma = 2
    else: carpma = 0

pgzrun.go()

