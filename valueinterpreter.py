class ValueInterpreter:

	under_min, over_max, over_max_left, over_max_right = 0, 0, 0, 0
	raw = [-1, -1, -1, -1, -1, -1, -1, -1]

	def push(self, values):
		THRESHOLD = 90
		MIN_TRESHOLD = 25

		self.raw = values

		self.under_min, self.over_max, self.over_max_left, self.over_max_right = 0, 0, 0, 0
		for i in range(len(values)):
			if values[i] > THRESHOLD:
				self.over_max += 1
			elif values[i] < MIN_TRESHOLD:
				self.under_min += 1
			if i in [0, 1]:
				self.over_max_left += 1
			elif i in [6, 7]:
				self.over_max_right += 1

	@property
	def peak_pos(self):
		return (-4, -3, -2, -1, 1, 2, 3, 4)[self.raw.index(max(self.raw))]

	@property
	def center_values(self):
		_, _, _, l, r, _, _, _ = self.raw
		return l, r

	@property
	def center_error(self):
		l, r = self.center_values
		return l - r

value_interpreter = ValueInterpreter()
