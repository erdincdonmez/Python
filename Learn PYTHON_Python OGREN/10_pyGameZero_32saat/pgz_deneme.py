import pygame
WIDTH = 300
HEIGHT = 250
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BRIGHT_BLUE = (0, 255, 255)
pygame.init() 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
clock = pygame.time.Clock()

running = True
while running :  
    #write your code here
    screen.fill(BLACK)   
    pygame.display.update()
    clock.tick(FPS)
    events = pygame.event.get()
    for i in events:
          if event.type == pygame.QUIT
                 running = False
pygame.quit()
