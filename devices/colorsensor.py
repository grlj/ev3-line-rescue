from ev3dev.ev3 import ColorSensor

class ColorSensor(ColorSensor):
	def __init__(self, port):
		super(ColorSensor, self).__init__(port)

	def calibrate(self):
		self.green = self.raw

	def is_green(self):
		current_value = self.raw
		if [abs(x - y) < 30 for x, y in zip(self.green, current_value)] == [True, True, True]:
			return True
		else:
			return False
