import os
import sys
imimport sys
import math
importport math
import pygame
import pygame.mixer
from pygame.locals import *

black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255

screen = screen_width, screen_height = 600, 400

clock = pygame.time.Clock()

pygame.display.set_caption("Physics")

fps_cap = 120
running = True
while running:
    clock.tick(fps_cap)

    for event in pygame.event.get(): #error is here
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)

    pygame.display.flip()

pygame.quit()
sys.exit    
#!/usr/bin/env python
