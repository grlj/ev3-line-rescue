from devices import driver as d, ultrasonic_sensor as us
from robotspecs import circumference as circ, robot_lenght

sharpturn = circ/4
x = robot_lenght/2 + 5
x2 = x + 2.5
y = robot_lenght + 20

def t1():
	while 1:
		if us.value() < 50:
			d.lr(circ/4, -circ/4, 6)
			d.lr(x, x, 6)
			d.lr(-circ/4, circ/4, 6)
			d.lr(y, y, 6)
			d.lr(-circ/4, circ/4, 6)
			d.lr(x2, x2, 6)
			d.lr(circ/4, -circ/4, 6)
