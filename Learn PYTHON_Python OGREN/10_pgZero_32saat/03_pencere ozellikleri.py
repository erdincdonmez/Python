import pgzrun
WIDTH = 400 # pencere genişliği
HEIGHT = 300 # pencere yüksekliği
TITLE = "Kristaller" # Oyunumuzun İsmi
FPS = 30 # Saniyedeki kare sayısı
def draw(): # ekran çizme fonksiyonu
    screen.clear() # ekranı temizle
    screen.fill("yellow") #rengin adı
    # screen.fill("#000000") #rengin kodu
    # screen.fill((0, 0, 0)) # rengin rgb (kym) renk gösterimindeki kodu
    screen.draw.circle((200, 150), 30, 'red')
pgzrun.go() 
