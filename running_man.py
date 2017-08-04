import pygame, sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

 # System parameters
FPS = 60
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SPEED = 5
PLATFORMY = SCREEN_HEIGHT - 150
# Game parameters
SPEED = 5
Y_VELOCITY_START = 20
Y_ACCELERATION = 0.5

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  

def get_events():
    jump = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            jump = True

    return jump

def update_logic(x, y, jump_pressed, yVelocity):
    if y >= PLATFORMY:
        y = PLATFORMY
        yVelocity = 0

    if y >= PLATFORMY:
        if jump_pressed == True:
            yVelocity = Y_VELOCITY_START
    else:
        yVelocity -= Y_ACCELERATION
        
    x += SPEED
    y -= yVelocity
    print y
    return x, y, yVelocity

def update_graphics(DISPLAYSURF, x, y):

    pygame.draw.rect(DISPLAYSURF, BLACK, (0, SCREEN_HEIGHT - 100, SCREEN_WIDTH, 100))
    pygame.draw.rect(DISPLAYSURF, BLUE, (x, y, 50, 50))

    pygame.display.update()

def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
    pygame.display.set_caption('Running Man!')
    fpsClock = pygame.time.Clock()

    x = 0
    y = PLATFORMY
    yVelocity = 0
    while True: # main game loop
        DISPLAYSURF.fill(WHITE)
        jump = get_events()

        x, y, yVelocity = update_logic(x, y, jump, yVelocity)

        update_graphics(DISPLAYSURF, x, y)

        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()