from util.bubblewrap import bubblewrap
from lib.statemachine import StateMachine
from states.lstripletlinefollowingstate import LineFollowingState


def test():
    StateMachine(LineFollowingState()).run()


run = bubblewrap(test)
