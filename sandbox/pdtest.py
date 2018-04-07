from devices import line_sensor_array as lsa, driver as d
from components.linedataparser import line_data_parser as ldp
from robotspecs import circumference
from components.pdcontroller import PDController as PD
from sandbox.devtools import rc, s, l, run_safe


S = 4
pd = PD(0.6, 3, 5)


def error_from_vector(vector):
	if sum(vector) == 0:
		return 0
	return sum([vector[i] * i for i in range(8)]) / sum(vector) - 3.5


def main():
	pd.reset()
	d.reset()

	while 1:
		rc.update()
		if rc.switch:
			pd.reset()
			continue

		raw = lsa.values()
		ldp.push(raw)
		if (ldp.repeat_count):
			continue
		# log()
		pd.push((d.average_position, error_from_vector(raw)))
		# print("{0:0.2f}".format(pd.error_derivative))

		d.set_speed(S, S * pd.value)

		# sc = ldp.split_count(ldp.origin_pos)
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


run_safe(main)
