class LineTracker:	
	raw = [-1, -1, -1, -1, -1, -1, -1, -1]
	mark_pos = 0

	def push(self, values):
		self.raw = values
		self.mark_pos = closest_active_bit(self.bits, self.mark_pos)

	@property
	def peak_pos(self):
		return self.raw.index(max(self.raw))

	@property
	def center_values(self):
		_, _, _, l, r, _, _, _ = self.raw
		return l, r

	@property
	def center_error(self):
		l, r = self.center_values
		return l - r

	def get_bits(self, threshold):
		return [(0,1)[v > threshold] for v in self.raw]

	@property
	def marks(self):
		return point_bits(self.mark_pos)

	@property
	def bits(self):
		return self.get_bits(70)  # TODO

	@property
	def peak(self):
		return point_bits(self.peak_pos)


	@property
	def sc(self):
		return split_count(self.bits, self.mark_pos)

	

def active_bits(vector):
	return [i for i, v in enumerate(vector) if v]

def closest_active_bit(vector, x):
	ab = active_bits(vector)
	if not len(ab):
		return -1
	return min(active_bits(vector), key=lambda x0:abs(x0-x))

def blank_bits():
	return [0, 0, 0, 0, 0, 0, 0, 0]

def split_count(vector, x):
	return vector[:x].count(1), vector[x+1:].count(1)

def point_bits(x):
	return [(0,1)[i==x] for i in range(len(blank_bits()))]
	

line_tracker = LineTracker()
