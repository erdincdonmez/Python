import pgzrun

WIDTH = 400 # pencere genişliği
HEIGHT = 300 # pencere yüksekliği
TITLE = "Oyun Adı" # Oyununuz için bir isim belirleyebilirsiniz
FPS = 30 # Saniyedeki kare sayısı

def draw():
    screen.clear()
    screen.draw.circle((200, 150), 30, 'red')

pgzrun.go()

