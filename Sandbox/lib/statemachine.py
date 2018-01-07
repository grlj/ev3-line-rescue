class StateMachine:
    def __init__(self, initial_state):
        self.state = initial_state

    def run(self):
        while self.state is not None:
            self.state = self.state.run()
