import pgzrun
from pgzero.actor import Actor
WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği
TITLE = "Uzaylı Yarışı" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı

# Nesneler
uzayli= Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))
new_image = 'uzaylı' # Mevcut Resmi Takip Eder
ari = Actor('uzaylı_arı', (850, 175)) # Arı

def draw():
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    ari.draw()
    
def update(dt):
    global new_image 
    if ari.x > -20: # Arının Hareketi
        ari.x = ari.x - 5
    else: ari.x = WIDTH + 20                
    
    if kutu.x > -20:# Kutunun Hareketi
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else: kutu.x = WIDTH + 20
        
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x =uzayli.x - 5
        if new_image != 'uzaylı_sol':
            uzayli.image = 'uzaylı_sol'
            new_image = 'uzaylı_sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if new_image != 'uzaylı_sağ':
            uzayli.image = 'uzaylı_sağ'
            new_image = 'uzaylı_sağ'
    elif keyboard.down or keyboard.s:
        if new_image != 'uzaylı_eğilme':
            uzayli.image = 'uzaylı_eğilme'
            new_image = 'uzaylı_eğilme'
            uzayli.y = 250
    else:
        if uzayli.y > 240 and new_image == 'uzaylı_eğilme':
            uzayli.image = 'uzaylı'
            new_image = 'uzaylı'
            uzayli.y = 240
        
def on_key_down(key): # Zıplama
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)

pgzrun.go() 



