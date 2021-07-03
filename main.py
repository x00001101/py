import pygame
from pygame.locals import *
from source.variable import *
from source.player import *


# Initialize program
pygame.init()
 
# Assign FPS a value
FPS = 60
clock = pygame.time.Clock()
 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("MyGame")

# load player
player = player(10,10)

# Beginning Game Loop
def main():

    run = True
    while run:
        clock.tick(FPS)
        screen.fill(DARKSLATEGREY)

        # load player
        player.render(screen)
        player.player_control_handling()

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
    
    pygame.quit()

if __name__ == "__main__":
    main()