from devices import driver as d, ultrasonic_sensor as us, line_sensor_array as lsa
from robotspecs import circumference as circ, robot_lenght

sharpturn = circ/4
x = robot_lenght/2 + 5
x2 = x + 2
y = robot_lenght + 12
THRESHOLD = 80

def evade():
	d.lr(circ/4, -circ/4, 6)
	d.lr(x, x, 6)
	d.lr(-circ/4, circ/4, 6)
	d.lr(y, y, 6)
	d.lr(-circ/4, circ/4, 6)
	d.lr(x2, x2, 6)
	d.lr(circ/4, -circ/4, 6)
	# if [i > THRESHOLD for i in lsa.values()].count(True) > 0:
	# 	return
	# else:
	# 	d.set_speed(0.5)
	# 	while 1:
	# 		if [i > THRESHOLD for i in lsa.values()].count(True) > 0:
	# 			d.stop()
	# 			return
