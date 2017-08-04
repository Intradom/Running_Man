import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

 # System parameters
FPS = 60

# Game parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 5

def get_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def update_logic(x):
    x += SPEED
    return x

def update_graphics(DISPLAYSURF, x):
    # Clear the screen
    DISPLAYSURF.fill(WHITE)
    
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
    pygame.draw.rect(DISPLAYSURF, BLUE, (x, SCREEN_HEIGHT - 150, 50, 50))

    pygame.display.update()

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    pygame.display.set_caption('Running Man!')
    fpsClock = pygame.time.Clock()

    x = 0
    while True: # main game loop
        get_events()

        x = update_logic(x)

        update_graphics(DISPLAYSURF, x)

        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()