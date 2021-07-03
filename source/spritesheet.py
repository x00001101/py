import pygame
from pygame.surfarray import blit_array
from source.variable import *

class spritesheet:
    def __init__(self, image_list):
        self.animation_delay = 120
        self.image_list = image_list
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.is_playing = False
    
    def load_image(self, frame, width, height, scale, colour = BLACK):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.image_list[frame], (0, 0))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image

    def update(self, screen):
        current_update = pygame.time.get_ticks()
        if current_update - self.last_update >= self.animation_delay:
            self.frame += 1
            self.last_update = current_update
            if self.frame >= len(self.image_list):
                self.frame = 0
        if self.is_playing == True:
            image = self.load_image(self.frame, 32, 32, 2)
        else:
            image = self.load_image(0, 32, 32, 2)
        screen.blit(image, (0,0))

    def play(self, is_playing = True):
        self.is_playing = is_playing