from devices import driver
from robotspecs import robot_specs as rs

FORWARD_SPEED = 6
TURNING_SPEED = 3
SHARP_TURN = rs["circumference"]/4
FORWARD_MOVE = 1

def do_left_sharp_turn():
	driver.stop()
	driver.reset()
	driver.lr(-SHARP_TURN, SHARP_TURN, TURNING_SPEED)
	driver.block()
	driver.reset()
	driver.lr(FORWARD_SPEED, FORWARD_SPEED, FORWARD_SPEED)
	driver.block()

def do_right_sharp_turn():
	driver.stop()
	driver.reset()
	driver.lr(SHARP_TURN, -SHARP_TURN, TURNING_SPEED)
	driver.block()
	driver.reset()
	driver.lr(FORWARD_SPEED, FORWARD_SPEED, FORWARD_SPEED)
	driver.block()
