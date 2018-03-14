from devices import driver
from devices import color_sensors as cs
from robotspecs import robot_specs as rs

SHARP_TURN = rs["circumference"]/8 - 0.7
FORWARD_SPEED = 10
TURNING_SPEED = 6

def crossing():
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
	print(left, right, back)
	if left > 8:
		driver.stop()
		driver.reset()
		driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
		driver.block()
		driver.reset()
		driver.lr(-SHARP_TURN, SHARP_TURN, TURNING_SPEED)
	elif right > 8:
		driver.stop()
		driver.reset()
		driver.lr(rs["color sensor y"], rs["color sensor y"], FORWARD_SPEED)
		driver.block()
		driver.reset()
		driver.lr(SHARP_TURN, -SHARP_TURN, TURNING_SPEED)
	elif back > 8:
		driver.stop()
		driver.reset()
		driver.lr(2*SHARP_TURN, -2*SHARP_TURN, TURNING_SPEED)

