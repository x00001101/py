import pygame
from source.variable import *
from source.spritesheet import *
from source.body2d import *

# images
PLAYER_IMAGES = {'_idle_anim_f':[], '_run_anim_f':[]} # name of the key is basically the part of filename. that makes it to easily get the full name while looping with just one for loop
sprite = {}
for image_key in PLAYER_IMAGES:
    for frame in range(4):
        PLAYER_IMAGES[image_key].append(pygame.image.load(os.path.join('assets', 'frames', PLAYER_SPRITE_NAME + image_key + str(frame) +'.png')))
    sprite[image_key] = spritesheet(PLAYER_IMAGES[image_key], 110)
IMAGE_WIDTH = PLAYER_IMAGES['_idle_anim_f'][0].get_width()


# collision box
body = body2d()

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
            spritesheet = sprite['_idle_anim_f']
        else:
            spritesheet = sprite['_run_anim_f']
        spritesheet.update(screen, self.x, self.y, self.flip)
        spritesheet.play()
    
    def player_control_handling(self):
        last_x = self.x # horizontal flip checker last
        last_pos = (self.x, self.y) # animation state checker last

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]: # left
            self.x -= self.movement_speed

        if keys[pygame.K_d]: # right
            self.x += self.movement_speed

        if keys[pygame.K_w]: # up
            self.y -= self.movement_speed

        if keys[pygame.K_s]: # down
            self.y += self.movement_speed

        cur_x = self.x # horizontal flip checker current
        cur_pos = (self.x, self.y) # animation state checker current

        if last_x > cur_x:
            self.flip = True
        elif last_x < cur_x:
            self.flip = False

        if last_pos != cur_pos:
            self.idle = False
        else:
            self.idle = True