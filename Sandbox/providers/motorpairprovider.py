from ev3dev.ev3 import Motor

from devices.motorpair import MotorPair
from lib.deviceproviders import provide_ev3_devices

motor_pair = MotorPair(*provide_ev3_devices(Motor, count=2, user='motor pair'))
FULL_TURN_TICKS = 1750
ONE_METER_TICKS = 2000
