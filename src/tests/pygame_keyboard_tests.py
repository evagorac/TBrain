import pygame
from pygame import K_LEFT, K_RIGHT, K_1, K_2, K_3, K_4, K_5, K_6
import time

pygame.display.init()
pygame.display.set_mode(size = (500,500))

while(True):
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        print('left')
    if keys[K_RIGHT]:
        print('right')
    if keys[K_UP]:
        print('up')
    if keys[K_DOWN]:
        print('down')
    time.sleep(.05)
    pygame.event.pump()
