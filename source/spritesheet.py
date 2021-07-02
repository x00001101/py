import pygame

class spritesheet:
    def __init__(self, image):
        self.sheet = image
    
    def get_image(self, width, height, scale, colour=(0,0,0)):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(colour)

        return image