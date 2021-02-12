import odrive as od
import time
import math
from odrive.enums import *

import setup

odrives = setup.import_odrives("odrive_serials.txt")

for odrive in odrives:
  for axis in [0,1]:
    setup.odrive_axis_calib(odrive, axis)

print("ok")

def do_sin(period, turn_mag):
  t0 = time.monotonic()
  while(True):
    set = turn_mag * math.sin((time.monotonic()-t0)*2*math.pi/period)
    print("set: " + str(set))
    print()
    for odrive in odrives:
      odrive.axis0.controller.input_pos = set
      odrive.axis1.controller.input_pos = set
    time.sleep(0.001)
do_sin(2, 1)
