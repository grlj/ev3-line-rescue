class StateMachine:
	def __init__(self, states):
		self.states = states

	def run(self, verbose=False):
		state = 'initial'

		if verbose:
			print('STATES:\n--> initial')

		while state != 'end':
			state = self.states[state]()
		
			if verbose:
				print('--> ' + state)

