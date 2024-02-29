import pgzrun
from pgzero.actor import Actor
# Pencerenin Çizimi
hucre = Actor("sınır")
hucre1 = Actor("zemin")
hucre2 = Actor("çatlak")
hucre3 = Actor("kemikler")
ekran_g = 7 # Ekranın enindeki hücre sayısı
ekran_y = 7 # Ekranın boyundaki hücre sayısı
WIDTH = hucre.width * ekran_g
HEIGHT = hucre.height * ekran_y

TITLE = "Zindanlar" # Oyunun Adı
FPS = 30 # Saniyedeki Kare Sayısı
haritam = [[0, 0, 0, 0, 0, 0, 0], 
           [0, 1, 2, 1, 3, 1, 0], 
           [0, 1, 1, 2, 1, 1, 0], 
           [0, 3, 2, 1, 1, 3, 0], 
           [0, 1, 1, 1, 3, 1, 0], 
           [0, 1, 3, 1, 1, 2, 0], 
           [0, 0, 0, 0, 0, 0, 0]]
          
karakter = Actor('karakter')
karakter.health = 100
karakter.attack = 5

def harita_cizim():
    for i in range(len(haritam)):
        for j in range(len(haritam[0])):
            if haritam[i][j] == 0:
                hucre.left = hucre.width*j
                hucre.top = hucre.height*i
                hucre.draw()
            elif haritam[i][j] == 1:
                hucre1.left = hucre.width*j
                hucre1.top = hucre.height*i
                hucre1.draw()
            elif haritam[i][j] == 2:
                hucre2.left = hucre.width*j
                hucre2.top = hucre.height*i
                hucre2.draw()  
            elif haritam[i][j] == 3:
                hucre3.left = hucre.width*j
                hucre3.top = hucre.height*i
                hucre3.draw() 

def draw():
    harita_cizim()
    karakter.draw()
    screen.draw.text(str(karakter.health), center=(325, 10), color = 'white', fontsize = 16)
    screen.draw.text(str(karakter.attack), center=(325, 25), color = 'white', fontsize = 16)

def on_key_down(key):
    if keyboard.right:
        karakter.x += hucre.width
        karakter.image = 'karakter'
    elif keyboard.left:
        karakter.x -= hucre.width
        karakter.image = 'sol'
    elif keyboard.down:
        karakter.y += hucre.height
    elif keyboard.up:
        karakter.y -= hucre.height

pgzrun.go()


