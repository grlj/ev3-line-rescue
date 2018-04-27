from ev3dev.ev3 import ColorSensor

class ColorSensor(ColorSensor):
	def __init__(self, port):
		super(ColorSensor, self).__init__(port)

	def values(self):
		return [self.value(i) for i in range(3)]

	def calibrate(self):
		self.mode = 'RGB-RAW'
		self.Green = self.values()

	def is_green(self):
		return False not in [abs(x - y) < 50 for x, y in zip(self.Green, self.raw)]