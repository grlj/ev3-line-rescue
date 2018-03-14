from manoeuvres.centralizefront import centralize_front as cf, fine_centralize as fc, skipping as sk
from devices import driver as d, line_sensor_array as lsa


def s():
	d.stop()

def log():
	print(lsa.values(), lsa.line_pos)
