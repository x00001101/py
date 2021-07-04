import pygame
from pygame.surfarray import blit_array
from source.variable import *

class spritesheet:
    def __init__(self, image_list, anim_delay, scale = 2):
        self.animation_delay = anim_delay
        self.image_list = image_list
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.is_playing = False
        self.loop = True
        self.scale = scale
    
    def load_image(self, frame, scale, flip, colour = BLACK):
        image_width = self.image_list[frame].get_width()
        image_height = self.image_list[frame].get_height()
        image = pygame.Surface((image_width, image_height)).convert_alpha()
        image.blit(self.image_list[frame], (0, 0))
        image = pygame.transform.scale(image, (image_width * scale, image_height * scale))
        if flip:
            image = pygame.transform.flip(image, True, False) # flip vertically
        image.set_colorkey(colour)

        return image

    def update(self, screen, x, y, flip = False):
        current_update = pygame.time.get_ticks()
        if current_update - self.last_update >= self.animation_delay:
            self.frame += 1
            self.last_update = current_update
            if self.frame >= len(self.image_list):
                if self.loop:
                    self.frame = 0
                else:
                    self.frame = len(self.image_list) - 1
        if self.is_playing == True:
            image = self.load_image(self.frame, self.scale, flip)
        else:
            image = self.load_image(0, self.scale, flip) # static first image if anim is not play
        screen.blit(image, (x,y))

    def play(self, is_playing = True, loop = True):
        self.is_playing = is_playing
        self.loop = loop
    
    def get_width(self):
        return self.image_list[0].get_width() * self.scale

    def get_height(self):
        return self.image_list[0].get_height() * self.scale