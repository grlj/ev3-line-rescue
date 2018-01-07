from lib.machinestate import MachineState
from states.sharpturnstate import SharpTurnState
from providers.motorpairprovider import motor_pair as mp
from providers.linesensortripletprovider import line_sensors
ls, ms, rs = line_sensors

SPEED = 200
THRESHOLD = 50


class LineFollowingState(MachineState):
    def run(self):
        while True:
            state = tuple([(0, 1)[r.value() < THRESHOLD] for r in (ls, ms, rs)])

            if state == (0, 1, 0):
                mp.set_speed(SPEED)
            elif state == (1, 0, 0):
                mp.set_speed(SPEED / 2, -SPEED / 2)
            elif state == (0, 0, 1):
                mp.set_speed(SPEED / 2, +SPEED / 2)
            elif state == (1, 1, 0):
                return SharpTurnState(-1)
            elif state == (0, 1, 1):
                return SharpTurnState(+1)

        return None
