import pygame
from source.variable import *

class body2d:
    def __init__(self):
        pass
    
    def render(self, x, y, width, height):
        body = pygame.Rect(x, y + height//2, width, height//2)