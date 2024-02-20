import pygame
 
FPS = 60
WIN_WIDTH = 500
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)

pygame.init()

clock = pygame.time.Clock()
 
sc = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
sc.fill(WHITE)
while True:

    events = pygame.event.get()
    for i in events:
        if i.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(sc, ORANGE, i.pos, 20)
            pygame.display.update()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1: print("Tıkladın")
    clock.tick(FPS)

