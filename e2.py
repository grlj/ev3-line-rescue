from manoeuvres.centralize import centralize as c, fine_centralize_lsa as fc, centralize_lsa as cl, centralize_axis as ca
from devices import driver as d, line_sensor_array as lsa
from valueinterpreter import value_interpreter as vi


def s():
	d.stop()

def log():
	print(lsa.values(), lsa.line_pos)
