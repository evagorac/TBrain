#!/usr/bin/env python3
from __future__ import print_function

import odrive as od
from odrive.enums import *
import time
import math

serial = "377236673137"

print("finding odrive with serial " + serial)
odrive = od.find_any(serial_number=serial)

print("calibrating axis 1:")

odrive.axis1.requested_state = AXIS_STATE_FULL_CALIBRATION_SEQUENCE
while odrive.axis1.current_state != AXIS_STATE_IDLE:
  time.sleep(0.1)

print("entering position control")
odrive.axis1.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# define pos setpoint squarewave
mag = 2 # revolutions
period = 2 # seconds

t0 = time.monotonic()
while(True):
  t = time.monotonic() % period
  if t < period/2:
    odrive.axis1.controller.input_pos = 0
  else:
    odrive.axis1.controller.input_pos = mag
