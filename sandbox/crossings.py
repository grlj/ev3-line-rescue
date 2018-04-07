from devices import driver, color_sensors as cs, line_sensor_array as lsa
from robotspecs import robot_specs as rs

SHARP_TURN = rs["circumference"]/8
FORWARD_SPEED = 10
TURNING_SPEED = 6
THRESHOLD = 80

def crossing():
	driver.stop()

	right = 0
	left = 0
	back = 0

	for i in range(10):
		detected_green = [i.is_green() for i in cs] 
		if detected_green == [True, True]:
			back += 1
		elif detected_green == [True, False]:
			left += 1
		elif detected_green == [False, True]:
			right += 1

	line_sensor_value = lsa.values()
	if line_sensor_value[3] > THRESHOLD or line_sensor_value[4]/2 > THRESHOLD:
		if left > 8:
			driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
			driver.lr(-SHARP_TURN, SHARP_TURN, TURNING_SPEED)
			driver.lr(0.5, 0.5, FORWARD_SPEED)

		elif right > 8:
			driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
			driver.lr(SHARP_TURN, -SHARP_TURN, TURNING_SPEED)
			driver.lr(0.5, 0.5, FORWARD_SPEED)

		elif back > 8:
			driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
			driver.lr(2*SHARP_TURN, -2*SHARP_TURN, TURNING_SPEED)

	if line_sensor_value[0] > THRESHOLD or line_sensor_value[1] > THRESHOLD:
		if left > 8:
			driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
			driver.lr(-SHARP_TURN, SHARP_TURN, TURNING_SPEED)
			driver.lr(0.5, 0.5, FORWARD_SPEED)


	elif line_sensor_value[6] > THRESHOLD or line_sensor_value[7] > THRESHOLD:
		if right > 8:
			driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
			driver.lr(SHARP_TURN, -SHARP_TURN, TURNING_SPEED)
			driver.lr(0.5, 0.5, FORWARD_SPEED)
