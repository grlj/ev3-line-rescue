from util.bitsetmanipulation import closest_active_bit

class FloatingMarker:
	pos = 3

	def push(self, bitset):
		cab = closest_active_bit(bitset, self.pos)

		if self.pos <= 0 and cab > 1:
			self.pos = -1

		elif self.pos >= 7 and cab < 6:
			self.pos = 8

		else:
			self.pos = cab

	@property
	def out_of_bounds(self):
		return self.pos not in range(8)
	

floating_marker = FloatingMarker()
