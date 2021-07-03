import pygame
from source.variable import *
from source.spritesheet import *

# images
OBJECT_IMAGES = []
OBJECT_SPRITE_NAME = 'chest_full_open_anim_f' # this is default character
for frame in range(3):
    OBJECT_IMAGES.append(pygame.image.load(os.path.join('assets', 'frames', OBJECT_SPRITE_NAME + str(frame) +'.png')))

class object:
    def __init__(self):
        self.properties = {}
    
    def render(screen):
        spritesheet.update(screen)
        spritesheet.play()