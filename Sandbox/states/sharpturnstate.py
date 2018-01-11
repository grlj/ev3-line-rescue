from util.robotutils import wait_until, set_led_color
#from util.robotutils import wait_until
from components.linecentering import line_centering as lc
from lib.machinestate import MachineState
from providers.motorpairprovider import motor_pair as mp
from providers.linesensortripletprovider import line_sensors
from providers.robotsizeprovider import distance_to_motor_rot as dtr, deg_to_motorpair_deg as detmd, SENSOR_TO_SENSOR, SENSOR_TO_AXLE
ls, ms, rs = line_sensors

import states.linefollowingstate  # fixes circular import issues

SPEED = 160
THRESHOLD = 50
RIGHT_ANGLE = 90

class SharpTurnState(MachineState):
    def __init__(self, turn):
        self.turn = turn

    def run(self):
        set_led_color('amber')

        mp.reset()
        mp.run_to_lr(dtr(SENSOR_TO_AXLE), dtr(SENSOR_TO_AXLE), SPEED)
        mp.block()
        #mp.set_speed(-SPEED, self.turn * SPEED)
        #wait_until(lambda: ms.value() < 70)
        #mp.stop()
        #mp.reset()
        mp.run_to_lr(self.turn*detmd(RIGHT_ANGLE), -self.turn*detmd(RIGHT_ANGLE), SPEED)
        mp.block()
        mp.reset()
        #mp.run_to_lr(dtr(SENSOR_TO_SENSOR), dtr(SENSOR_TO_SENSOR), SPEED)
        #mp.block()
        lc()
        mp.block()
        return states.linefollowingstate.LineFollowingState()
