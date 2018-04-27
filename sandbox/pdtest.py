from devices import line_sensor_array as lsa, driver as d, color_sensors as cs
# ultrasonic_sensor as us
from components.linedataparser import line_data_parser as ldp
from robotspecs import circumference
from util.linedatamanipulation import error_from_vector
from components.pdcontroller import PDController as PD
from sandbox.devtools import s, l, run_safe
from sandbox.crossings import crossing as cross
from time import sleep
from sandbox.evasion_manouver import evade

S = 4
pd = PD(0.35, 3, 3)

cs[0].Green = [101, 122, 81]
cs[1].Green = [93, 123, 64]

def main():

	# us.mode = "US-DIST-CM"
	c = 0
	pd.reset()
	d.reset()

	while 1:
		sleep(0.0001)
		if c%4 == 0:
			# if us.value() < 50:
			# 	evade()
			# 	pd.reset()
			cs_value = [i.values() for i in cs]
			detected_green = [False not in [abs(x - y) < 50 for x, y in zip(cs[i].Green, cs_value[i])] for i in range(2)]
			if detected_green[0] or detected_green[1]:
				print("crossing")
				cross()
				pd.reset()
				d.reset()
		c+=1
		# detected_green = [i.is_green() for i in cs]
		# green_component_detected = [abs(cs_value[i][1] - cs[i].Green[1]) < 20 for i in range(2)]
		raw = lsa.values()
		ldp.push(raw)

		# if [i > 75 for i in raw].count(True) > 6:
		# 	d.lr(1.2, 1.2, 5)
		# 	pd.reset()
		# 	d.reset()

		# elif green_component_detected[0] or green_component_detected[1]:
		# 	scan_lr()
		# 	if abs(cs[0].values()[1] - cs[0].Green[1]) < 20 or abs(cs[1].values()[1] - cs[1].Green[1]) < 20:
		# 		d.lr(0.5, 0.5, 5)
		# 		scan_lr()
		# 	pd.reset()

		if (ldp.repeat_count):
			if (ldp.repeat_count > 10):
				print("SENZOR JE ODKSAOASFNFNGJJL<CSAmj")
			continue
		
		error = error_from_vector(raw) if max(raw) > 10 else 0

		pd.push((d.average_position, error))
		
		d.set_speed(S, S * pd.value)


def m1(w):
	return d.lr(w * circumference / 4, -w * circumference / 4, 6).lr(2, 2, 6)

def t():
	run_safe(main)
