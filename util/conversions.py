from math import pi

def distance_to_motor(distance, wheel_radius):
	return (distance/wheel_radius)*(180/pi)

def motor_to_distance(motor_value, wheel_radius):
	return motor_value * wheel_radius * pi / 180
