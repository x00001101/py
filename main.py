import pygame, sys
from pygame import sprite
from pygame.locals import *
from source.variable import *
from source.spritesheet import *

# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 60
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("MyGame")

# display 
spritesheet = spritesheet(PLAYER_IMAGE[0])

PLAYER_SPRITE = spritesheet.get_image(32, 32, 2)

# Beginning Game Loop
def main():

    run = True
    while run:
        clock.tick(FPS)
        screen.fill(LIGHTSLATEGREY)
        screen.blit(PLAYER_SPRITE, (10,10))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()