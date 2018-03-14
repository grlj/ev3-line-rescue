from ev3dev.ev3 import ColorSensor

class ColorSensor(ColorSensor):
	green = 2
	def __init__(self, port):
		super(ColorSensor, self).__init__(port)

	def color_value(self):
			self.mode = "COL-COLOR"
			return self.value()

	def calibrate(self):
		self.green = self.color_value()

	def is_green(self):
		if self.value() == self.green:
			return True
		else:
			return False
