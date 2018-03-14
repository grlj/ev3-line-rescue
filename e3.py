from devices import driver
from devices import line_sensor_array as lsa, color_sensors as cs
from valueinterpreter import value_interpreter
from robotspecs import robot_specs as rs
from crossings import crossing

THRESHOLD = 90
FORWARD_SPEED = 10
TURNING_SPEED = 6
SHARP_TURN = rs["circumference"]/16

def line_follow():
	while 1:
		value = lsa.values()
		direction = 1
		index = value.index(max(value))
		value_interpreter.push(values=value)
		detected_green = tuple([i.is_green() for i in cs])

		if index in [0, 1, 2]:
			direction = -1
		elif index in [5, 6, 7]:
			index = 7 - index

		if detected_green[0] or detected_green[1]:
			driver.stop()
			driver.reset()
			driver.lr(0.5, 0.5, 0.5)
			driver.block()
			crossing()

		elif value_interpreter.under_min == 8:
			pass # no line detected
		elif value_interpreter.over_max > 2:
			if value_interpreter.over_max_left > 0 and value_interpreter.over_max_right > 0:
				pass # crossing while going throu
			elif value_interpreter.over_max_left > 0 and (value[3] > THRESHOLD or value[4] > THRESHOLD): # left sharp turn
				driver.stop()
				driver.reset()
				driver.lr(-SHARP_TURN, SHARP_TURN, TURNING_SPEED)
				print("left sharpturn")
			elif value_interpreter.over_max_right > 0 and (value[3] > THRESHOLD or value[4] > THRESHOLD): # right sharp turn
				driver.stop()
				driver.reset()		
				driver.lr(SHARP_TURN, -SHARP_TURN, TURNING_SPEED)
				print("right sharpturn")
		elif (value[3] + value[4]) / 2 > THRESHOLD: # line centred
			driver.set_speed(FORWARD_SPEED)
		else: # line uncentred
			driver.set_speed(FORWARD_SPEED*((index)/3), direction*TURNING_SPEED*(1/(index+1)))

def stop():
	driver.stop()
