from devices import line_sensor_array as lsa, driver as d
from components.linedataparser import line_data_parser as ldp
from util.logbitsets import log_bitsets
from util.linedatamanipulation import active_bits
from util.mouse import mouse as m
from util import rc

def s():
	d.stop()


def l():
	ldp.push(lsa.values())
	log()


def log():
	log_bitsets({'*':active_bits(ldp.raw), '+':ldp.line_bitset, '@':ldp.origin, 'P':ldp.peak})

def run_safe(fun):
	try:
		fun()
	except KeyboardInterrupt:
		s()