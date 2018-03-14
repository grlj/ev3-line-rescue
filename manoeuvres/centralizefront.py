from devices import driver, line_sensor_array as lsa
from robotspecs import robot_specs as rs


def centralize_front():
	driver.set_speed(turning=5)
	while lsa.line_pos != 0:
		print(lsa.line_pos)
	driver.stop()
	return


circ = rs['circumference']
FC_SPEED = 3
T = 70

# def fineCentralize():
# 	while 1:
# 		_,_,_,l,r,_,_,_ = lsa.values()
# 		if l > r:
# 			driver.set_speed(turning=-FC_SPEED)
# 		else:
# 			driver.set_speed(turning=FC_SPEED)


def fine_centralize():
	driver.reset()
	driver.stop_action = 'hold'
	driver.lr(-circ / 6, circ / 6, FC_SPEED)
	
	pos, error = (0, 0), 100
	while driver.running():
		_,_,_,l,r,_,_,_ = lsa.values()
		new_error = abs(l - r)
		
		if new_error > error + 10:
			break

		if (l > T or r > T) and new_error < error:
			error = new_error
			pos = driver.position

	driver.lr(*pos, speed=FC_SPEED)

	return pos, error

def skipping():
	while 1:
		_,_,_,l,r,_,_,_ = lsa.values()
		if (l < r):
			driver.skip(+100)
		else:
			driver.skip(-100)
		driver.block()

