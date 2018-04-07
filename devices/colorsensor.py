from ev3dev.ev3 import ColorSensor

class ColorSensor(ColorSensor):
	def __init__(self, port):
		super(ColorSensor, self).__init__(port)

	def values(self):
		return (self.value(i) for i in range(3))

	def calibrate(self):
		self.mode = 'RGB-RAW'
		self.Green = self.values()

	def is_green(self):
		current_value = self.values()
		if [abs(x - y) < 30 for x, y in zip(self.Green, current_value)] == [True, True, True]:
			return True
		else:
			return False
