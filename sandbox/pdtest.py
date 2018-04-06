from devices import line_sensor_array as lsa, driver as d
from linedatainterpreter import line_data_interpreter as ldi
from logbitsets import log_bitsets
from linedatamanipulation import active_bits
from robotspecs import circumference
from pdcontroller import PDController as PD


pd = PD(0.6, 3, 5)

def s():
	d.stop()


def a():
	ldi.push(lsa.values())
	log()	


def log():
	log_bitsets({'*':active_bits(ldi.raw), '+':ldi.line_bitset, '@':ldi.origin, 'P':ldi.peak})


def error_from_vector(vector):
	return sum([vector[i] * i for i in range(8)]) / sum(vector) - 3.5

def t():
	try:
		c()
	except KeyboardInterrupt:
		s()

S = 4
l1 = True
def c():
	pd.reset()
	d.reset()

	while 1:
		raw = lsa.values()
		ldi.push(raw)
		if (ldi.repeat_count):
			continue
		# log()
		pd.push((d.average_position, error_from_vector(raw)))
		# print("{0:0.2f}".format(pd.error_derivative))

		d.set_speed(S, S * pd.value)

		# sc = ldi.split_count(ldi.origin_pos)
		# w = sc[1] - sc[0]

		# if abs(w) > 2:
		# 	if w < 0:
		# 		print('LLLLLLLL')
		# 		m1(-1)
		# 	if w > 0:
		# 		print('RRRRRRRR')
		# 		m1(1)

		# elif l3 or l2 or l1:
		# 	d.set_speed(2, turning=-2)

		# elif l0 or r0:
		# 	d.set_speed(3)

		# elif r1 or r2 or r3:
		# 	d.set_speed(2, turning=2)


def m1(w):
	return d.lr(w * circumference / 4, -w * circumference / 4, 6).lr(2, 2, 6)