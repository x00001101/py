import pygame
from source.variable import *
from source.spritesheet import *

# images
PLAYER_SPRITE_NAME = 'knight_f_' # this is default character
PLAYER_IMAGES = {'idle_anim_f':[], 'run_anim_f':[]}
for image_key in PLAYER_IMAGES:
    for frame in range(4):
        PLAYER_IMAGES[image_key].append(pygame.image.load(os.path.join('assets', 'frames', PLAYER_SPRITE_NAME + image_key + str(frame) +'.png')))

spritesheet_idle = spritesheet(PLAYER_IMAGES['idle_anim_f'])
spritesheet_run = spritesheet(PLAYER_IMAGES['run_anim_f'])

class player:
    def __init__(self, x, y):
        # self.properties = {}
        self.x = x
        self.y = y
        self.idle = True
        self.flip = False # flip sprite if move left
        self.movement_speed = 3
    
    def render(self, screen):
        if self.idle == True:
            spritesheet = spritesheet_idle
        else:
            spritesheet = spritesheet_run
        spritesheet.update(screen, self.x, self.y, self.flip)
        spritesheet.play()
    
    def player_control_handling(self):
        last_x = self.x
        last_y = self.y

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left
            self.flip = True
            self.x -= self.movement_speed

        if keys[pygame.K_d]: # right
            self.flip = False
            self.x += self.movement_speed

        if keys[pygame.K_w]: # up
            self.y -= self.movement_speed

        if keys[pygame.K_s]: # down
            self.y += self.movement_speed

        cur_x = self.x
        cur_y = self.y

        if last_x != cur_x or last_y != cur_y:
            self.idle = False
        elif last_x == cur_x or last_y == cur_y:
            self.idle = True