from devices import driver, lineSensorArray


def centralizeFront():
	driver.set_speed(turning=5)
	while lineSensorArray.line_pos != 0:
		print(lineSensorArray.line_pos)
	driver.stop()
	return
