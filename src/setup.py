import odrive as od
from odrive.enums import *
from odrive.utils import *
import time
import math

# this file implements relevant functions for setting up odrives

def import_odrive_axes(file):
  # accepts file name to txt of odrive serials
  # returns list of all 3 odrive objects, ordered from from bottom to top physically
  # ---------------------------------------

  # import saved serial numbers for odrive differentiation
  # ordered from bottom of the stack to the top
  odrive_serials = []
  f = open(file, 'r')
  Lines = f.readlines()

  for line in Lines:
    # remove linefeed character
    line = line[:-1]
    if line == '':
      break
    odrive_serials.append(line)
  f.close()

  odrives = []
  for serial in odrive_serials:
    print("finding odrive with serial number: " + str(serial))
    odrive = od.find_any(serial_number = serial)
    odrives.append(odrive)

  return odrives

def get_axis_object(odrive, axis):
  if axis == 0:
    axis_object = odrive.axis0
  elif axis == 1:
    axis_object = odrive.axis1
  else:
    raise("no such axis " + str(axis))

def odrive_axis_calib(odrive, axis, full_calib=True):
  # given odrive object and axis (0,1), calibrate and enter position control mode

  axis_object = get_axis_object(odrive, axis)

  print("calibrating axis " + str(axis) + " for odrive " + str(hex(odrive.serial_number)))

  axis_object.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
  while axis_object.current_state != AXIS_STATE_IDLE:
    time.sleep(0.1)

  if axis_object.error != 0:
    print('\033[91m')
    print("error calibrating axis " + str(axis) + " for odrive " + str(hex(odrive.serial_number)) + " with error code " + str(axis_object.error))
    print("encoder error: " + str(axis_object.encoder.error))
    print("motor error: " + str(axis_object.motor.error))
    print('\033[0m')
    raise Exception("calibration failed")

  axis_object.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

def clear_errors(odrive):
  dump_errors(odrive,True)

def flash_settings(odrive):
  # flash good values for settings
  print("flashing settings to odrive " + str(hex(odrive.serial_number)))
  for axis in [odrive.axis0, odrive.axis1]:
    axis.controller.config.pos_gain = 80
    axis.controller.config.vel_gain = .12
    axis.controller.config.vel_integrator_gain = .25
    axis.controller.config.vel_limit = 50000
    axis.motor.config.current_lim = 10
  odrive.save_configuration()

#def flash_propdrive_settings(odrive):
#  # flash good PID values
#  # these should be looked over again
#  for config in [odrive.axis0.controller.config, odrive.axis1.controller.config]
#    config.pos_gain = 75
#    config.vel_gain = .1
#    config.vel_integrator_gain = .3
#  odrive.save_configuration()

if __name__ == "__main__":
  odrives = import_odrives("odrive_serials.txt")
  # test calib all axes
  for odrive in odrives:
    flash_settings(odrive)
    for axis in [0,1]:
      odrive_axis_calib(odrive, axis)
