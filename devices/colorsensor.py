from ev3dev.ev3 import ColorSensor

class ColorSensor(ColorSensor):
	green = 2
	def __init__(self, port):
		super(ColorSensor, self).__init__(port)

	def calibrate(self):
		self.green = self.raw

	def is_green(self):
		return False not in [abs(x - y) < 10 for x, y in zip(self.green, self.raw)]
