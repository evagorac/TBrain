import setup
from odrive.utils import *

odrives = setup.import_odrives("odrive_serials.txt")

for odrive in odrives:
  print("clearing errors for odrive " + str(odrive.serial_number))
  setup.clear_errors(odrive)
  print()
  print()
