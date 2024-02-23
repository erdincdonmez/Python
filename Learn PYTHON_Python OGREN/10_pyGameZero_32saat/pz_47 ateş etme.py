import pgzrun
from pgzero.actor import Actor
import random
WIDTH = 600
HEIGHT = 450
TITLE = "Space Journey"
FPS = 30
gemi = Actor("gemi", (300, 400))
space = Actor("uzay")
enemies = []
planets = [Actor("gezegen1", (random.randint(0, 600), -100)), Actor("gezegen2", (random.randint(0, 600), -100)), Actor("gezegen3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("gemi1", (100, 200))
type2 = Actor("gemi2", (300, 200))
type3 = Actor("gemi3", (500, 200))

for i in range(5):# Making the düşman list
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    düşman = Actor("düşman", (x, y))
    düşman.speed = random.randint(2, 8)
    enemies.append(düşman)
    
for i in range(5):# Making the meteor list
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

def draw():# Drawing up
    if mode == 'menu':# Starting menu screen
        space.draw()
        screen.draw.text('Select a ship', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    if mode == 'game':# Game mode
        space.draw()
        planets[0].draw()
        for i in range(len(meteors)):# Drawing meteors up
            meteors[i].draw()
        gemi.draw()
        for i in range(len(enemies)):# Drawing enemies up
            enemies[i].draw()
        for i in range(len(bullets)):# Drawing projectiles up 
            bullets[i].draw()
    elif mode == 'end':# Game over window 
        space.draw()
        screen.draw.text("KAYBETTİNİZ!", center = (300, 200), color = "white", fontsize = 36)
    
def on_mouse_move(pos):# Controls
    gemi.pos = pos

def new_düşman():# Adding new enemies to the list
    x = random.randint(0, 400)
    y = -50
    düşman = Actor("düşman", (x, y))
    düşman.speed = random.randint(2, 8)
    enemies.append(düşman)

def düşman_gemi():# düşman movement
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_düşman()

def planet():# Planet movement
    if planets[0].y < 550:
            planets[0].y = planets[0].y + 1
    else:
        planets[0].y = -100
        planets[0].x = random.randint(0, 600)
        first = planets.pop(0)
        planets.append(first)

def meteorites():# Meteor movement
    for i in range(len(meteors)):
        if meteors[i].y < 450:
            meteors[i].y = meteors[i].y + meteors[i].speed
        else:
            meteors[i].x = random.randint(0, 600)
            meteors[i].y = -20
            meteors[i].speed = random.randint(2, 10)

def collisions():# Collisions
    global mode
    for i in range(len(enemies)):
        if gemi.colliderect(enemies[i]):
            mode = 'end'

def update(dt):
    if mode == 'game':
        düşman_gemi()
        collisions()
        planet()
        meteorites()
        for i in range(len(bullets)):# Projectile movement
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y = bullets[i].y - 10

def on_mouse_down(button, pos):
    global mode, gemi
    if mode == 'menu' and type1.collidepoint(pos):
        gemi.image = "gemi1"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        gemi.image = "gemi2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        gemi.image = "gemi3"
        mode = 'game'
    elif mode == 'game' and button == mouse.LEFT:# Shooting 
        bullet = Actor("missiles")
        bullet.pos = gemi.pos
        bullets.append(bullet)
pgzrun.go()
