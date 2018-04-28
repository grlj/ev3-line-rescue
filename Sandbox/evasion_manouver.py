from devices import driver as d, line_sensor_array as lsa
from robotspecs import circumference as circ, robot_lenght

sharpturn = circ/4
x = robot_lenght/2 + 5 # x should be the lenght from the lsa to robot back + a bit extra 
y = robot_lenght + 0 + 0 + 5 # should be robot lenght + us threshold distance + obsticle width + a bit extra
THRESHOLD = 60

def evade():
	d.lr(circ/4, -circ/4, 6)
	d.lr(x, x, 6)
	d.lr(-circ/4, circ/4, 6)
	d.lr(y, y, 6)
	d.lr(-circ/4, circ/4, 6)
	while 1:
		if [i > THRESHOLD for i in lsa.values()].count(True) > 0:
			d.stop()
			break
		else:
			d.set_speed(6, 0.05)
	d.lr(circ/4, -circ/4, 6)
	# if [i > THRESHOLD for i in lsa.values()].count(True) > 0:
	# 	return
	# else:
	# 	d.set_speed(0.5)
	# 	while 1:
	# 		if [i > THRESHOLD for i in lsa.values()].count(True) > 0:
	# 			d.stop()
	# 			return
