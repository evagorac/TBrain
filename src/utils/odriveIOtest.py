import odrive as od
import setup

# test functionality of inputs.  each input is connected to GPIO 3 and 4 of each odrive.

odrives = setup.import_odrives("../odrive_serials.txt")

while True:
    volts = []
    for odrive in odrives:
        for pin in range(3,5):
            volts.append(odrive.get_adc_voltage(pin))
    for val in volts:
        print(val > 1.5)
    print()


