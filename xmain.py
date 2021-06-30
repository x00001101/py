import os
import pygame
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()
window = pygame.display.set_mode((640,480))
title = pygame.display.set_caption("My game")
# ^^^ sing kudu onok

x = 120
y = 120

speed = 10

running = True

while running:
    
    for event in pygame.event.get():
    	if event.type == pygame.QUIT:
    		running = False
    		break
    	elif event.type == pygame.KEYDOWN:
    		if event.key == pygame.K_ESCAPE:
    			running = False
    			break
    		elif event.key == pygame.K_d:
    			x += speed
    		elif event.key == pygame.K_a:
    			x -= speed
    		elif event.key == pygame.K_s:
    			y += speed
    		elif event.key == pygame.K_w:
    			y -= speed

    	window.fill((0,0,0))
    	pygame.draw.rect(window, (255,0,0), (x, y, 200, 150))
    	pygame.display.update()

pygame.quit()