#from util.robotutils import wait_until
from lib.machinestate import MachineState
from providers.motorpairprovider import motor_pair as mp
from providers.linesensortripletprovider import line_sensors
from providers.robotsizeprovider import distance_to_motor_rot as dtr, deg_to_motorpair_deg as detmd, SENSOR_TO_SENSOR, SENSOR_TO_AXLE
ls, ms, rs = line_sensors

import states.linefollowingstate # fixes circular import issues

SPEED = 160
THRESHOLD = 50
RIGHT_ANGLE = 90

class SharpTurnState(MachineState):
    def __init__(self, turn):
        self.turn = turn

    def run(self):
        print("gsfdssd")
        mp.reset()
        mp.run_to_lr(dtr(SENSOR_TO_AXLE), dtr(SENSOR_TO_AXLE), SPEED)
        mp.block()
        #mp.set_speed(-SPEED, self.turn * SPEED)
        #wait_until(lambda: ms.value() < THRESHOLD)
        #mp.stop()
        mp.reset()
        print("iadfuudfsailuasf")
        print(str(detmd(RIGHT_ANGLE)))
        mp.run_to_lr(self.turn*detmd(RIGHT_ANGLE), -self.turn*detmd(RIGHT_ANGLE), SPEED)
        mp.block()
        mp.reset()

        print("eztzerr")
        mp.run_to_lr(dtr(SENSOR_TO_SENSOR), dtr(SENSOR_TO_SENSOR), SPEED)
        mp.block()
        return states.linefollowingstate.LineFollowingState()