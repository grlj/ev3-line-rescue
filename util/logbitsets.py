from util.bitsetmanipulation import blank_bitset


def log_bitsets(bitset_dict):
	message = ['_' for _ in blank_bitset()]
	for new_char, bitset in bitset_dict.items():
		message = [new_char if active else old_char for old_char, active in zip(message, bitset)]
	print(''.join(message))