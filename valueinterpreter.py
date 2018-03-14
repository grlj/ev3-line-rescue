class ValueInterpreter:

	under_min, over_max, over_max_left, over_max_right = 0, 0, 0, 0

	def push(self, values):
		THRESHOLD = 90
		MINTRESHOLD = 25

		self.under_min, self.over_max, self.over_max_left, self.over_max_right = 0, 0, 0, 0
		for i in range(len(values)): # constructs interpreted
			if values[i] > THRESHOLD:
				self.over_max += 1
				if i in [0, 1]:
					self.over_max_left += 1
				elif i in [6, 7]:
					self.over_max_right += 1
			elif values[i] < MINTRESHOLD:
				self.under_min += 1


value_interpreter = ValueInterpreter()
