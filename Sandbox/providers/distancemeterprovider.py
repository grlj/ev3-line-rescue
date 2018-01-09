from ev3dev.ev3 import UltrasonicSensor as US

from lib.deviceproviders import provide_ev3_devices

front_distance_meter = tuple(provide_ev3_devices(US, count=1, user='front facing ultrasonic sensor'))
