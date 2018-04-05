from linedatamanipulation import active_bits, isolated_cluster, peak_pos, bitset_from_pos, split_count
from floatingmarker import FloatingMarker


class LineDataParser:
	def __init__(self):
		self.origin_marker = FloatingMarker()
		self.raw = []

	def push(self, data):
		if data == self.raw:
			self.repeat_count += 1
			return
		self.repeat_count = 0
		self.raw = data
		self.isolated = self.raw
		self.isolated = isolated_cluster(self.raw, self.origin_pos)
		self.line_bitset = active_bits(self.isolated)
		self.peak_pos = peak_pos(self.isolated)
		self.origin_marker.push(self.line_bitset)

	@property
	def origin_pos(self):
		return self.origin_marker.pos

	@property
	def origin(self):
		return bitset_from_pos(self.origin_pos)

	@property
	def peak(self):
		return bitset_from_pos(self.peak_pos)

	def split_count(self, split_pos):
		return split_count(self.line_bitset, split_pos)


line_data_parser = LineDataParser()
