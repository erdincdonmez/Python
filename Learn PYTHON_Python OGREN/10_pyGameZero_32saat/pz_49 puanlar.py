import pgzrun
from pgzero.actor import Actor
import random
WIDTH = 600
HEIGHT = 450
TITLE = "Space Journey"
FPS = 30
ship = Actor("ship1", (300, 400))
space = Actor("space")
enemies = []
planets = [Actor("plan1", (random.randint(0, 600), -100)), Actor("plan2", (random.randint(0, 600), -100)), Actor("plan3", (random.randint(0, 600), -100))]
meteors = []
bullets = []
mode = 'menu'
type1 = Actor("ship1", (100, 200))
type2 = Actor("ship2", (300, 200))
type3 = Actor("ship3", (500, 200))
count = 0

for i in range(5):# Making the enemy list
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)
    
for i in range(5):# Making the meteor list
    x = random.randint(0, 600)
    y = random.randint(-450, -50)
    meteor = Actor("meteor", (x, y))
    meteor.speed = random.randint(2, 10)
    meteors.append(meteor)

def draw():# Drawing up
    if mode == 'menu':# Starting meny screen
        space.draw()
        screen.draw.text('Choose the ship', center = (300, 100), color = "white", fontsize = 36)
        type1.draw()
        type2.draw()
        type3.draw()
    if mode == 'game':# game mode
        space.draw()
        planets[0].draw()
        for i in range(len(meteors)):# Drawing meteors up
            meteors[i].draw()
        ship.draw()
        for i in range(len(enemies)):# Drawing enemies up
            enemies[i].draw()
        for i in range(len(bullets)):# Drawing projectiles up 
            bullets[i].draw()
        screen.draw.text(str(count), (10, 10), color = "white")
    elif mode == 'end':# Game over window 
        space.draw()
        screen.draw.text("GAME OVER!", center = (300, 200), color = "white", fontsize = 36)
        screen.draw.text(str(count), center = (300, 250), color = "white", fontsize = 64)
    
def on_mouse_move(pos):# Controls
    ship.pos = pos

def new_enemy():# Adding new enemies to the list
    x = random.randint(0, 400)
    y = -50
    enemy = Actor("enemy", (x, y))
    enemy.speed = random.randint(2, 8)
    enemies.append(enemy)

def enemy_ship():# Enemy movement
    for i in range(len(enemies)):
        if enemies[i].y < 650:
            enemies[i].y = enemies[i].y + enemies[i].speed
        else:
            enemies.pop(i)
            new_enemy()

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
    global count
    for i in range(len(enemies)):
        if ship.colliderect(enemies[i]):
            mode = 'end'
        for j in range(len(bullets)):# Projectile collisions
            if bullets[j].colliderect(enemies[i]):
                count = count + 1
                enemies.pop(i)
                bullets.pop(j)
                new_enemy()
                break

def update(dt):
    if mode == 'game':
        enemy_ship()
        collisions()
        planet()
        meteorites()
        for i in range(len(bullets)):# Projectile movement
            if bullets[i].y < 0:
                bullets.pop(i)
                break
            else:
                bullets[i].y -= 10
        
def on_mouse_down(button, pos):
    global mode, ship
    if mode == 'menu' and type1.collidepoint(pos):
        ship.image = "ship1"
        mode = 'game'
    elif mode == 'menu' and type2.collidepoint(pos):
        ship.image = "ship2"
        mode = 'game'
    elif mode == 'menu' and type3.collidepoint(pos):
        ship.image = "ship3"
        mode = 'game'
      
    elif mode == 'game' and button == mouse.LEFT:# Shooting 
        bullet = Actor("missiles")
        bullet.pos = ship.pos
        bullets.append(bullet)

pgzrun.go()
