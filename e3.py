from devices import driver
from devices import line_sensor_array as lsa
from valueinterpreter import value_interpreter
from robotspecs import robot_specs as rs

THRESHOLD = 90
MINTRESHOLD = 25
FOWARDSPEED = 10
TURNINGSPEED = 6
SHARPTURN = rs["circumference"]/8 - 1

def line_follow():
	while 1:
		value = lsa.values()
		direction = 1
		index = value.index(max(value))
		value_interpreter.push(value)

		if index in [0, 1, 2]:
			direction = -1
		else:
			index = 7 - index

		if value_interpreter.under_min == 8:
			pass # no line detected
		elif value_interpreter.over_max > 2:
			if value_interpreter.over_max_left > 0 and value_interpreter.over_max_right > 0:
				print("crossing")
				pass # TODO križišča
			elif value_interpreter.over_max_left > 0 and (value[3] > THRESHOLD or value[4] > THRESHOLD): # left sharpturn
				driver.lr(-SHARPTURN, SHARPTURN, TURNINGSPEED)
				print("left sharpturn")
			elif value_interpreter.over_max_right > 0 and (value[3] > THRESHOLD or value[4] > THRESHOLD): # right sharpturn
				driver.lr(SHARPTURN, -SHARPTURN, TURNINGSPEED)
				print("right sharpturn")
		elif (value[3] + value[4]) / 2 > THRESHOLD: # line centred
			driver.set_speed(FOWARDSPEED)
		else: # line uncentred
			driver.set_speed(FOWARDSPEED*((index)/3), direction*TURNINGSPEED*(1/(index+1)))

def stop():
	driver.stop()
