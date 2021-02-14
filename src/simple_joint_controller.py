import pygame
from utils import setup
import numpy
import odrive as od
import time

#odrives = import_odrives("odrive_serials.txt")

#for odrive in odrives:
#    for axis in [0,1]:
#        odrive_axis_calib(odrive, axis)

current_joint = 1

while(True):
    print(pygame.key.get_pressed())
    time.sleep(.25)
