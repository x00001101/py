from source.body2d import body2d
import pygame
from source.variable import *
from source.spritesheet import *
from source.body2d import *

# images
OBJECT_IMAGES = []
OBJECT_SPRITE_NAME = 'chest_full_open_anim_f' # this is default character
for frame in range(3):
    OBJECT_IMAGES.append(pygame.image.load(os.path.join('assets', 'frames', OBJECT_SPRITE_NAME + str(frame) +'.png')))

spritesheet = spritesheet(OBJECT_IMAGES, 500)
body = body2d()

class object:
    def __init__(self, x, y):
        self.properties = {}
        self.x = x
        self.y = y
    
    def render(self, screen):
        spritesheet.update(screen, self.x, self.y)
        spritesheet.play(True, False)