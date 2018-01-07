from util.robotutils import wait_until
from lib.machinestate import MachineState
from providers.motorpairprovider import motor_pair as mp
from providers.linesensortripletprovider import line_sensors
from providers.robotsizeprovider import distance_to_motor_rot, SENSOR_TO_SENSOR, SENSOR_TO_AXLE
import states
LineFollowingState = states.lstripletlinefollowingstate.LineFollowingState
ls, ms, rs = line_sensors

SPEED = 160
THRESHOLD = 50
DISTANCE_1 = 235
DISTANCE_2 = 51

class SharpTurnState(MachineState):
    def __init__(self, turn):
        self.turn = turn

    def run(self):
        mp.reset()
        mp.run_to_lr(distance_to_motor_rot(SENSOR_TO_AXLE), distance_to_motor_rot(SENSOR_TO_AXLE), SPEED)
        mp.block()
        mp.set_speed(-SPEED, self.turn * SPEED)
        wait_until(lambda: ms.value() < THRESHOLD)
        mp.stop()
        mp.reset()
        mp.run_to_lr(distance_to_motor_rot(SENSOR_TO_SENSOR), distance_to_motor_rot(SENSOR_TO_SENSOR), SPEED)
        mp.block()
        return None