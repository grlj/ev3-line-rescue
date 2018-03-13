from lib.statemachine import StateMachine

def test():
	print('testis')
	return 'end'


robot = StateMachine({
	'initial': lambda: 'line following',
	'line following': test,
	'sharp turn': None,
})

robot.run(verbose=True)
