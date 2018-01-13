from time import time

measurements = {}

def value_proto(self):
	v = super(self.__class__.base_class, self).value()
	if id(self) not in measurements:
		measurements[id(self)] = []
	measurements[id(self)].append((time(), v))
	return v

def hooked_sensor_class(sensor_class):
	c = type('Hooked' + sensor_class.__name__, (sensor_class,), {'value': value_proto})
	c.base_class = sensor_class
	return c
