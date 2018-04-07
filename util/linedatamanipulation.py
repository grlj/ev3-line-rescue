from .bitsetmanipulation import *

ISOLATED_CLUSTER_THRESHOLD = 20
def isolated_cluster(vector, cluster_pos):
	new_vector = 8 * [0]
	for i in range(cluster_pos, len(vector)):
		new_vector[i] = vector[i]
		if vector[i] < ISOLATED_CLUSTER_THRESHOLD:
			break

	for i in range(cluster_pos)[::-1]:
		new_vector[i] = vector[i]
		if vector[i] < ISOLATED_CLUSTER_THRESHOLD:
			break

	return new_vector


def error_from_vector(vector):
	if sum(vector) == 0:
		return 0
	return sum([vector[i] * i for i in range(8)]) / sum(vector) - 3.5


def peak_pos(vector):
	return vector.index(max(vector))


ACTIVE_BITS_THRESHOLD = 75
def active_bits(vector):
	return [(0,1)[v > ACTIVE_BITS_THRESHOLD] for v in vector]



