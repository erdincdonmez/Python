import pgzrun
from pgzero.actor import Actor
from keyboard import is_pressed
WIDTH = 600  
HEIGHT = 300  
TITLE = "Uzaylı Koşusu"  
FPS = 30  

uzayli = Actor('uzaylı', (50, 240))
arkaplan = Actor("uzaylı_arkaplan")
kutu = Actor('uzaylı_kutu', (550, 265))
yeni_resim = 'uzaylı'  
ari = Actor('uzaylı_arı', (850, 175))
ob = Actor("uzaylı_oyunbitti")
oyun_sonu = 0
puan = 0
bitis_puani = 0

def draw():
    global bitis_puani
    global puan
    arkaplan.draw()
    uzayli.draw()
    kutu.draw()
    ari.draw()
    if oyun_sonu == 1:
        if bitis_puani == 0 : bitis_puani = puan;
        ob.draw()
        screen.draw.text(f"Enter'a Basınız. Puanınız:{bitis_puani}", pos=(170, 230), color= "red", fontsize = 36)
        screen.draw.text('Kutuya çarptınız', pos=(230, 250), color= "white", fontsize = 36)
    elif oyun_sonu == 2:
        if bitis_puani == 0 : bitis_puani = puan;
        ob.draw()
        screen.draw.text(f"Enter'a Basınız. Puanınız:{bitis_puani}", pos=(170, 230), color= "red", fontsize = 36)
        screen.draw.text('Arıya çarptınız', pos=(230, 250), color= "white", fontsize = 36)

def update(dt):
    global yeni_resim
    global oyun_sonu
    global puan
    if ari.x > -20: ari.x = ari.x - 5        
    else:
        ari.x = WIDTH + 20
        puan = puan + 1
       
    if kutu.x > -20:
        kutu.x = kutu.x - 5
        kutu.angle = kutu.angle + 5
    else:
        kutu.x = WIDTH + 20
        puan = puan + 1
       
    if keyboard.left or keyboard.a and uzayli.x > 20:
        uzayli.x = uzayli.x - 5
        if yeni_resim != 'uzaylı_sol':
            uzayli.image = 'uzaylı_sol'
            yeni_resim = 'uzaylı_sol'
    elif keyboard.right or keyboard.d and uzayli.x < 580:
        uzayli.x = uzayli.x + 5
        if yeni_resim != 'uzaylı_sağ':
            uzayli.image = 'uzaylı_sağ'
            yeni_resim = 'uzaylı_sağ'
    elif keyboard.down or keyboard.s:
        if yeni_resim != 'uzaylı_eğilme':
            uzayli.image = 'uzaylı_eğilme'
            yeni_resim = 'uzaylı_eğilme'
            uzayli.y = 250
    else:
        if uzayli.y > 240 and yeni_resim == 'uzaylı_eğilme':
            uzayli.image = 'uzaylı'
            yeni_resim = 'uzaylı'
            uzayli.y = 240
   
    # if oyun_sonu == 1 and is_pressed('enter'): # Sadece kutuya çarptığında
    if oyun_sonu > 0  and is_pressed('enter'): # Kutuya veya arıya çarptığında
        oyun_sonu = 0
        puan = 0
        uzayli.pos = (50, 240)
        kutu.pos = (550, 265)
        kutu.pos = (850, 175)
   
    if uzayli.colliderect(kutu) and oyun_sonu==0:
        oyun_sonu = 1
    elif uzayli.colliderect(ari) and oyun_sonu==0:
        oyun_sonu = 2
       
def on_key_down(key):
    if keyboard.space or keyboard.up or keyboard.w:
        uzayli.y = 0
        animate(uzayli, tween='bounce_end', duration=2, y=240)

pgzrun.go()
