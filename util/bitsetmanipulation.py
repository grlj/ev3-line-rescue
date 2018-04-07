def active_bits(bitset):
	return [i for i, v in enumerate(bitset) if v]

def closest_active_bit(bitset, x):
	ab = active_bits(bitset)
	if not len(ab):
		return -1
	return min(active_bits(bitset), key=lambda x0:abs(x0-x))

def blank_bitset():
	return 8 *[0]

def split_count(bitset, x):
	return bitset[:x].count(1), bitset[x+1:].count(1)

def bitset_from_pos(x):
	return [(0,1)[i==x] for i in range(len(blank_bitset()))]
