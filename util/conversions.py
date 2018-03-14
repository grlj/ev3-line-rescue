from math import pi
from robotspecs import robot_specs as rs

def distance_to_motor(distance):
	return (distance/rs['wheel radius'])*(180/pi)

def motor_to_distance(motor_pos):
	return motor_pos * rs['wheel radius'] * pi / 180
