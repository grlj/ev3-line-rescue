from devices import line_sensor_array as lsa, driver as d
from valueinterpreter import value_interpreter as vi

def s():
	d.stop()

def a():
	vi.push(lsa.values())
	print(vi.sc)

def c():
	while 1:
		vi.push(lsa.values())
		l3, l2, l1, l0, r0, r1, r2, r3 = vi.peak

		if vi.sc[0] > 2:
			d.set_speed(turning=-3)
			print('LLLLLL')

		if vi.sc[1] > 2:
			d.set_speed(turning=3)
			print('RRRRRR')

		elif l3 or l2 or l1:
			d.set_speed(-1, turning=-2)

		elif l0 or r0:
			d.set_speed(3)

		elif r1 or r2 or r3:
			d.set_speed(-1, turning=2)
