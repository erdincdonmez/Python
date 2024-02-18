import pgzrun
from pgzero.actor import Actor
WIDTH = 300 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği
TITLE = "Kaledeki Hayalet"
FPS = 30 

hayalet = Actor('hayalet', (150, 150))
arkaplan = Actor("hayalet_arkaplan")

def draw():
    arkaplan.draw()
    hayalet.draw()

def update(dt):
    if keyboard.left and hayalet.x > 20: hayalet.x -= 5        
    elif keyboard.right and hayalet.x < 280: hayalet.x += 5
    elif keyboard.up and hayalet.y > 20: hayalet.y -= 5
    elif keyboard.down and hayalet.y < 280: hayalet.y += 5
       
def on_key_down(key):    
    if keyboard.space and hayalet.image == 'hayalet1':
        hayalet.image = 'hayalet'
    elif keyboard.space and hayalet.image == 'hayalet':
        hayalet.image = 'hayalet1'

pgzrun.go()
