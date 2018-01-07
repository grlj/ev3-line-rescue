from lib.machinestate import MachineState
from providers.motorpairprovider import motor_pair as mp
from providers.linesensorpairprovider import line_sensors
ls, rs = line_sensors

SPEED = 200
THRESHOLD = 50
TOLERANCE = 20


class LineFollowingState(MachineState):
    def run(self):
        while True:
            mp.set_speed(SPEED)
            while True:
                if ls.value() < THRESHOLD:
                    mp.set_speed(SPEED / 2, -SPEED / 2)
                    while ls.value() < THRESHOLD + TOLERANCE:
                        pass
                    break

                if rs.value() < THRESHOLD:
                    mp.set_speed(SPEED / 2, +SPEED / 2)
                    while rs.value() < THRESHOLD + TOLERANCE:
                        pass
                    break
        return None
