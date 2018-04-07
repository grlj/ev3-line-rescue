from .mouse import mouse as m
from devices import driver as d

def run_left():
	d.left.run_forever(speed_sp=600)

def run_right():
	d.right.run_forever(speed_sp=600)

def stop_left():
	d.left.stop()

def stop_right():
	d.right.stop()

def run_backward():
	d.left.run_forever(speed_sp=-600)
	d.right.run_forever(speed_sp=-600)

def stop_both():
	d.stop()

def run():
	try:
		m.update_loop()
	except KeyboardInterrupt:
		d.stop()

m.left_press = run_right
m.left_release = stop_right
m.right_press = run_left
m.right_release = stop_left
m.extra_press = run_backward
m.extra_release = stop_both
