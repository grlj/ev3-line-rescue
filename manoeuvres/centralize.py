from devices import driver, line_sensor_array as lsa, central_line_sensor as ls
from valueinterpreter import value_interpreter as vi


def centralize():
	centralize_lsa()
	fine_centralize_lsa()


# from robotspecs import robot_specs as rs
# circ = rs['circumference']
# FC_SPEED = 3
# T = 70

# def fine_centralize2(speed=FC_SPEED):
# 	driver.reset()
# 	driver.stop_action = 'hold'
# 	driver.lr(-circ / 6, circ / 6, speed)
	
# 	pos, error = (0, 0), 100
# 	while driver.running():
# 		_,_,_,l,r,_,_,_ = lsa.values()
# 		new_error = abs(l - r)

# 		if new_error > error + 10:
# 			print('asdf')
# 			break

# 		if (l > T or r > T) and new_error < error:
# 			error = new_error
# 			pos = driver.position

# 	driver.lr(*pos, speed=speed)
# 	driver.skip(-speed)

# 	return pos, error

FC_SPD = 3
def centralize_lsa():
	driver.stop_action = 'hold'
	while 1:
		vi.push(lsa.values())

		if (vi.peak_pos < 0):
			driver.set_speed(turning=-FC_SPD)
		else:
			driver.set_speed(turning=+FC_SPD)

		if abs(vi.peak_pos) <= 1 and abs(vi.center_error) < 5:
			driver.stop()
			return


def fine_centralize_lsa():
	while 1:
		vi.push(lsa.values())
		print(vi.center_error)
		if (vi.center_error < -1):
			driver.skip(+100)
		elif (vi.center_error > 1):
			driver.skip(-100)
		else:
			pass
		driver.block()

		# TODO break


def centralize_axis():
	driver.reset()
	driver.stop_action = 'hold'
	driver.lr(5, 5, 3)

	max_val, pos = 0, (0, 0)
	while driver.running():
		val = 100 - ls.value()
		if val > max_val:
			max_val = val
			pos = driver.position

	driver.lr(*pos, speed=3)
	driver.block()
