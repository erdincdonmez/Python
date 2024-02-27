import pgzrun
from pgzero.actor import Actor
WIDTH = 600
HEIGHT = 400

TITLE = "Hayvan Avcısı"
FPS = 30

# Nesneler
hayvan = Actor("zürafa", (150, 250))
arkaplan = Actor("arkaplan")
bonus_1 = Actor("bonus", (450, 100))
bonus_2 = Actor("bonus", (450, 200))

# Değişkenler
puan = 0
tiklama = 1

def draw():
    arkaplan.draw()
    hayvan.draw()
    screen.draw.text(str(puan), center=(150, 100), color="white", fontsize = 96)
    bonus_1.draw()
    screen.draw.text("Her 2 saniye için 1$", center=(450, 80), color="black", fontsize = 20)
    screen.draw.text("Ücret : 15 Puan", center=(450, 110), color="black", fontsize = 20)
    bonus_2.draw()
    screen.draw.text("Her 2 saniye için 15$", center=(450, 180), color="black", fontsize = 20)
    screen.draw.text("Ücret : 200$", center=(450, 210), color="black", fontsize = 20)

def bonus_1_icin():
    global puan
    puan += 1

def bonus_2_icin():
    global puan
    puan += 15

def on_mouse_down(button, pos):
    global puan
    if button == mouse.LEFT:
        # Hayvanın üzerinde tıklama
        if hayvan.collidepoint(pos):
            puan += tiklama
            hayvan.y = 200
            animate(hayvan, tween='bounce_end', duration=0.5, y=250)
        # bonus_1 butonu tıklandığında  
        elif bonus_1.collidepoint(pos):
            if puan >= 15:
                schedule_interval(bonus_1_icin, 2)
                puan -= 15
        # bonus_1 butonu tıklandığında 
        elif bonus_2.collidepoint(pos):
            if puan >= 200:
                schedule_interval(bonus_2_icin, 2)
                puan -= 200
pgzrun.go()
# Belirli bir sayıdaki saniyeden sonra her hangi bir fonksiyonun çağırılması için schedule_interval() fonksiyonu kullanılır.
# Parantezlerin içerisine, ne kadar saniye sonra hangi fonksiyonun çağırılacağı yazılır:
# schedule_interval(isim, 2)
# İki tane fonksiyon oluşturun: bonus_1_icin() - her iki saniyede bir 1$ ekleyecek olan birinci bonus için kullanılacak, bonus_2_icin() - her iki saniyede bir 15$ ekleyecek olan birinci bonus için kullanılacak.
# Sonrasında, butona tıklanmasını ve bonusun alınabilecek olup olmadığını kontrol edecek olan bir koşul yazacağız, çünkü alışveriş eğer hesapta yeterli miktarda para varsa gerçekleşmeli.
# Eğer yeterli miktar varsa, puan azaltılacak ve fonksiyon çalışmaya başlayacak - şimdi her iki saniyede bir puanımız artacak.
# Bonusları istediğiniz kadar alabilirsiniz. Örneğin, birinci bonusu iki sefer alırsanız puanını her iki saniyede bir $2 artacak.
# Kodunuzu yazdıktan sonra onu kopyalayın çünkü bir sonraki alıştırmada ihtiyacınız olacak.
# 60169

