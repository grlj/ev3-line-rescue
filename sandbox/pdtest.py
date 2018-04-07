from devices import line_sensor_array as lsa, driver as d, color_sensors as cs
from components.linedataparser import line_data_parser as ldp
from robotspecs import circumference
from util.linedatamanipulation import error_from_vector
from components.pdcontroller import PDController as PD
from sandbox.devtools import s, l, run_safe
from sandbox.crossings import crossing as cross

S = 4
pd = PD(0.6, 3, 5)

cs[0].Green = (161, 224, 112)
cs[1].Green = (201, 260, 151)

def main():
	pd.reset()
	d.reset()

	while 1:
		detected_green = [i.is_green() for i in cs]
		raw = lsa.values()
		ldp.push(raw)

		if [i > 75 for i in raw].count(True) > 6:
			d.lr(1, 1, 5)
			pd.reset()

		if detected_green[0] or detected_green[1]:
			cross()
			pd.reset()

		if (ldp.repeat_count):
			if (ldp.repeat_count > 10):
				print("SENZOR JE ODKSAOASFNFNGJJL<CSAmj")
			continue
		
		pd.push((d.average_position, error_from_vector(raw)))
		
		d.set_speed(S, S * pd.value)


def m1(w):
	return d.lr(w * circumference / 4, -w * circumference / 4, 6).lr(2, 2, 6)

def t():
	run_safe(main)
