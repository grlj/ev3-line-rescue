from ev3dev.ev3 import ColorSensor as CS

from lib.deviceproviders import provide_ev3_devices

line_sensors = tuple(provide_ev3_devices(CS, count=3, user='line sensor triplet'))
