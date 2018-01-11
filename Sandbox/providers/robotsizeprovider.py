from math import pi

#all units in cm
WHEEL_RADIUS = 2.8
AXLE_LENGHT = 15.0
SENSOR_TO_SENSOR = 2.5
SENSOR_TO_AXLE = 5.7

def distance_to_motor_rot(d): # d in cm
	return (d/WHEEL_RADIUS)*(180/pi)

def deg_to_motorpair_deg(fi): # fi in deg motors rotating in opposite direction
	return (AXLE_LENGHT/WHEEL_RADIUS)/(fi*4)
	