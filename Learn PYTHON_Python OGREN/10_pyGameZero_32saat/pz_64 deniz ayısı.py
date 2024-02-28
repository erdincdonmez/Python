import pgzrun
from pgzero.actor import Actor
from pgzero.clock import schedule_interval
WIDTH = 600
HEIGHT = 400

TITLE = "Hayvan Avcısı"
FPS = 30

# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))
bonus_3 = Actor("bonus", (450, 300))
oyna = Actor("oyna", (300, 100))
carpi = Actor("çarpı", (580, 20))
magaza = Actor("mağaza", (300, 200))
koleksiyon = Actor("koleksiyon", (300, 300))
timsah = Actor('timsah', (120, 200))
suaygiri = Actor('suaygırı', (300, 200))
denizayisi = Actor('denizayısı', (480, 200))

# Değişkenler
puan = 0
tiklama = 1
mod = 'menü'
ucret_1 = 15
ucret_2 = 200
ucret_3 = 600
hayvanlar = []

def draw():
    if mod == 'menü':
        arkaplan.draw()
        oyna.draw()
        screen.draw.text(str(puan), center=(30, 20), color="white", fontsize = 36)
        magaza.draw()
        koleksiyon.draw()
   
    elif mod == 'oyun':    
        arkaplan.draw()
        hayvan.draw()
        screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)
        bonus_1.draw()
        screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
        screen.draw.text(str(ucret_1), center=(450, 110), color="black", fontsize = 20)
        bonus_2.draw()
        screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
        screen.draw.text(str(ucret_2), center=(450, 210), color="black", fontsize = 20)
        bonus_3.draw()
        screen.draw.text("Her 2 saniye için 50$", center=(450, 280), color="black", fontsize = 20)
        screen.draw.text(str(ucret_3), center=(450, 310), color="black", fontsize = 20)
        carpi.draw()
    
    elif mod == 'mağaza':
        arkaplan.draw()
        timsah.draw()
        screen.draw.text("500$", center= (120, 300), color="white", fontsize = 36)
        suaygiri.draw()
        screen.draw.text("2500$", center= (300, 300), color="white", fontsize = 36)
        denizayisi.draw()
        screen.draw.text("7000$", center= (480, 300), color="white", fontsize = 36)
        carpi.draw()
        screen.draw.text(str(puan), center=(30, 20), color="white", fontsize = 36)
    
    elif mod == 'koleksiyon':
        arkaplan.draw()
        for i in range(len(hayvanlar)):
            hayvanlar[i].draw()
        carpi.draw()
        screen.draw.text(str(puan), center=(30, 20), color="white", fontsize = 36)
        screen.draw.text("+2$", center= (120, 300), color="white", fontsize = 36)
        screen.draw.text("+3$", center= (300, 300), color="white", fontsize = 36)
        screen.draw.text("+4$", center= (480, 300), color="white", fontsize = 36)

def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def bonus_3_icin():
    global puan
    puan += 50

def on_mouse_down(button, pos):
    global puan
    global mod
    global ucret_1, ucret_2, ucret_3
    global tiklama
    # Oyun Modu
    if button == mouse.LEFT and mod == "oyun":
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
       # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            bonus_1.y = 105
            animate(bonus_1, tween='bounce_end', duration=0.5, y=100)
            if puan >= ucret_1:
                schedule_interval(bonus_1_icin, 2)
                puan -= ucret_1
                ucret_1 *= 2
        # bonus_2 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            bonus_2.y = 205
            animate(bonus_2, tween='bounce_end', duration=0.5, y=200)
            if puan >= ucret_2:
                schedule_interval(bonus_2_icin, 2)
                puan -= ucret_2
                ucret_2 *= 2
        # bonus_3 button tıklandığında
        elif bonus_3.collidepoint(pos):
            bonus_3.y = 305
            animate(bonus_3, tween='bounce_end', duration=0.5, y=300)
            if puan >= ucret_3:
                schedule_interval(bonus_3_icin, 2)
                puan -= ucret_3
                ucret_3 *= 2
        elif carpi.collidepoint(pos):
            mod = 'menü'
    # Menü Modu
    elif mod == 'menü' and button == mouse.LEFT:
        if oyna.collidepoint(pos):
            mod = 'oyun'
        elif magaza.collidepoint(pos):
            mod = 'mağaza'
        elif koleksiyon.collidepoint(pos):
            mod = "koleksiyon"
    
    # Mağaza        
    elif  mod == 'mağaza' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        # Timsahın Seçilmesi
        elif timsah.collidepoint(pos):
            if timsah in hayvanlar:
                hayvan.image = 'timsah'
            elif puan >= 500:
                puan -= 500
                tiklama = 2
                hayvan.image = 'timsah'
                hayvanlar.append(timsah)
         # Su Aygırının Seçilmesi  
        elif suaygiri.collidepoint(pos):
            if suaygiri in hayvanlar:
                hayvanlar.image = 'suaygiri'
            elif puan >= 2500:
                puan -= 2500
                tiklama = 3
                hayvan.image = 'suaygırı'
                hayvanlar.append(suaygiri)
        # Deniz Ayısının Seçilmesi   
        elif denizayisi.collidepoint(pos):
            if denizayisi in hayvanlar:
                hayvan.image = 'denizayısı'
            elif puan >= 7000:
                puan -= 7000
                tiklama = 4
                hayvan.image = 'denizayısı'
                hayvanlar.append(denizayisi)
                
    # Koleksiyon
    elif  mod == 'koleksiyon' and button == mouse.LEFT:
        if carpi.collidepoint(pos):
            mod = 'menü'
        # Timsahın Seçilmesi
        elif timsah.collidepoint(pos):
            if timsah in hayvanlar:
                hayvan.image = 'timsah'
                
        # Su Aygırının Seçilmesi    
        elif suaygiri.collidepoint(pos):
            if suaygiri in hayvanlar:
                hayvan.image = 'suaygırı'
        # Deniz Ayısının Seçilmesi
        elif denizayisi.collidepoint(pos):
            if denizayisi in hayvanlar:
                hayvan.image = 'denizayısı'
pgzrun.go()