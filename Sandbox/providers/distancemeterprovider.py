from ev3dev.ev3 import UltrasonicSensor as us

from lib.deviceproviders import provide_ev3_device

front_distance_meter = provide_ev3_device(us, user='front facing ultrasonic sensor')
