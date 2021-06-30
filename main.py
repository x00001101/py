import pygame, sys
from pygame.locals import *
from source.variable import *

# Initialize program
pygame.init()

# Initialize color from variable
color = color()
BGCOLOR = color.get_color("WHITE")
 
# Assign FPS a value
FPS = 60
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("MyGame")
 
# Beginning Game Loop
while True:
    screen.fill(BGCOLOR)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    FramePerSec.tick(FPS)