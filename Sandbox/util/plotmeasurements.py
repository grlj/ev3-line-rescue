import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
from lib.measurements import measurements

def save_plot(path='measurements/default_plot.png'):
	print('Saving plot ... ')
	for m in measurements.values():
		a = list(zip(*m))
		plt.plot(a[0], a[1], '-o')

	plt.savefig(path, bbox_inches='tight')
	print('done')
