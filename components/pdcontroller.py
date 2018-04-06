from collections import deque

X, Y = 0, 1

class PDController:
	def __init__(self, p, d, history_length):
		self.p = p
		self.d = d
		self.history = deque([], history_length)

	def reset(self):
		self.history.clear()

	@property
	def history_length(self):
		return len(self.history)

	@history_length.setter
	def history_length(self, new_length):
		self.history = deque(self.history, new_length)

	@property
	def error_derivative(self):
		distance = self.history[-1][X] - self.history[0][X]
		error_change = self.history[-1][Y] - self.history[0][Y]

		if not distance:
			return 0

		return error_change / distance

	@property
	def error(self):
		return self.history[0][Y]

	def push(self, pt):
		self.history.append((pt))

	@property
	def p_component(self):
		return self.error * self.p

	@property
	def d_component(self):
		return self.error_derivative * self.d

	@property
	def value(self):
		return self.p_component + self.d_component
