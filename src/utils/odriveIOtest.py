import odrive as od
import setup

''' we will test the funcitonality of the GPIO pins on the odrives for ease of wiring, all inputs to the system (homing switches, etc.) are connected to the top odrive on the stack.  we will print the state of each input (currently 6 for each joint homing switch)'''

odrives = setup.import_odrives("../odrive_serials.txt")

while True:
    volts = []
    for odrive in odrives:
        for pin in range(3,5):
            volts.append(odrive.get_adc_voltage(3,4))
    for val in volts:
        print(val)
    print()


