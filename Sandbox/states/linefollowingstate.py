from lib.machinestate import MachineState
from providers.motorpairprovider import motor_pair as mp
from util.robotutils import set_led_color
from providers.linesensortripletprovider import line_sensors
from providers.distancemeterprovider import front_distance_meter as fdm
ls, ms, rs = line_sensors

import states.sharpturnstate # fixes circular import issues
import states.evasionstate # fixes circular import issues

SPEED = 200
THRESHOLD = 50
STEERING = 0.7
DISTANCE_THRESHOLD = 70

class LineFollowingState(MachineState):
    def run(self):
        set_led_color('green')

        state = (0, 1, 0)

        while True:
            readings = tuple([(0, 1)[r.value() < THRESHOLD] for r in (ls, ms, rs)])

            if readings not in ((0, 0, 0), (1, 1, 1)):
                state = readings

            if state == (0, 1, 0): 
                mp.set_speed(SPEED)
            elif state == (1, 0, 0):
                mp.set_speed(SPEED / 2, -SPEED * STEERING)
            elif state == (0, 0, 1):
                mp.set_speed(SPEED / 2, +SPEED * STEERING)
            elif state == (1, 1, 0):
                return states.sharpturnstate.SharpTurnState(-1)
            elif state == (0, 1, 1):
                return states.sharpturnstate.SharpTurnState(+1)
            if fdm.value() < DISTANCE_THRESHOLD:
                return states.evasionstate.EvasionState()
