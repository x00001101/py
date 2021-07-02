import os
import pygame

# color variables
BLACK = (0,0,0)
WHITE = (255,255,255)
DARKSLATEGREY  = (47,79,79)
LIGHTSLATEGREY = (119,136,153)
DIMGREY = (105,105,105)
GREY = (128,128,128)

# images
PLAYER_IMAGE = []
PLAYER_SPRITE_NAME = 'knight_m_idle_anim_f' # this is default character
for frame in range(0,3):
    PLAYER_IMAGE.append(pygame.image.load(os.path.join('assets', 'frames', PLAYER_SPRITE_NAME + str(frame) +'.png')))