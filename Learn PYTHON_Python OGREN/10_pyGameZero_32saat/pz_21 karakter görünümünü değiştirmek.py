import pgzrun
from pgzero.actor import Actor

WIDTH = 600 
HEIGHT = 300 
TITLE = "Uzaylı Yarışı" # Oyunun Adı 
FPS = 30 # Saniyedeki kare sayısı

uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    
def update(dt):
    global new_image # !!! GLOBAL DEĞİŞKEN
    
    if kutu.x > - 20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else: kutu.x = WIDTH + 20
    
    if keyboard.left and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        # NOT: Burada yazılı olan kontroller düzgün çalışabilmesi için
        if new_image != 'uzaylı_sol':
            uzayli.image = 'uzaylı_sol'
            new_image = 'uzaylı_sol'
    elif keyboard.right and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if new_image != 'uzaylı_sağ':
            uzayli.image = 'uzaylı_sağ'
            new_image = 'uzaylı_sağ'
    else:
        uzayli.image = 'uzaylı'
        new_image = 'uzaylı'

def on_key_down(key): # Zıplama        
    if keyboard.space:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

pgzrun.go() 



