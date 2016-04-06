__author__ = 'brown'

import pygame,os

pygame.font.init()

WIDTH = 1280
HEIGHT = 750
FPS = 60

RED    = (255,  0,  0)
GREEN  = (  0,255,  0)
BLUE   = (  0,  0,255)
GREY   = (180,180,200)

FONT_SM = pygame.font.Font(os.path.join('fonts', 'ccaps.ttf'), 70)
FONT = pygame.font.Font(os.path.join('fonts', 'ccaps.ttf'), 100)