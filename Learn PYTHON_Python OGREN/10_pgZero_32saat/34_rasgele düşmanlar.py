import pgzrun
from pgzero.actor import Actor
from keyboard import is_pressed
import random

WIDTH = 600 # Pencere Genişliği
HEIGHT = 300 # Pencere Yüksekliği
TITLE = "Uzaylı Koşusu" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayı

uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))
ari = Actor('uzaylı_arı', (850, 175))
ob = Actor("uzaylı_oyunbitti")
# Değişkenler
oyun_sonu = 0
puan = 0
dusman = random.randint(1,2)

def kutular():
    global puan
    global dusman
    if kutu.x > -20: # Kutu Hareketleri
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
        puan = puan + 1
        dusman = random.randint(1,2)
        
def arilar():
    global puan
    global dusman
    if ari.x > -20:# Arı Hareketleri
        ari.x = ari.x - 5
    else:
        ari.x = WIDTH + 20
        puan = puan + 1
        dusman = random.randint(1,2)

def draw():
    arkaplan.draw()
    uzayli.draw()
    if dusman == 1:
        kutu.draw()
    else: ari.draw()
    screen.draw.text(str(puan) , pos=(10, 10), color="white", fontsize = 24)
    if oyun_sonu == 1:
        ob.draw()
        screen.draw.text("Enter'a Basınız", pos=(170, 250), color= "red", fontsize = 36)

def update(dt): # Değişkenler
    global oyun_sonu
    global puan
    
    # Fonksiyonların Çağrılması
    if dusman == 1: kutular()
    else: arilar()
    
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        uzayli.image = 'uzaylı_sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        uzayli.image = 'uzaylı_sağ'
    elif keyboard.down or keyboard.s:
        uzayli.image = 'uzaylı_eğilme'
        uzayli.y = 250
    else:
        uzayli.image = 'uzaylı'
        if uzayli.y > 240:
            uzayli.y = 240
    
    if oyun_sonu == 1 and is_pressed('enter'):
        oyun_sonu = 0 
        puan = 0
        uzayli.pos = (50, 240)
        kutu.pos = (550, 265)
        ari.pos = (850, 175)
    
    if uzayli.colliderect(kutu) or uzayli.colliderect(ari):
        oyun_sonu = 1
        
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 100
        animate(uzayli, tween='bounce_end', duration=2, y=240)
        
pgzrun.go()

