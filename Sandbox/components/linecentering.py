from lib.machinestate import MachineState
from util.robotutils import wait_until
from providers.motorpairprovider import motor_pair as mp
from providers.linesensortripletprovider import line_sensors
ls, ms, rs = line_sensors

SPEED = 50
THRESHOLD = 70
LINE_THRESHOLD = 20
STEERING = 0.75

def line_centering():
    state = tuple([(0, 1)[r.value() < THRESHOLD] for r in (ls, ms, rs)])

    print(state, ls.value(), ms.value(), rs.value())

    if state != (0, 1, 0):     
        if ls.value() < ms.value():
                mp.set_speed(0, -SPEED)
                wait_until(lambda: ms.value() < LINE_THRESHOLD)
                mp.stop()
        elif rs.value() < ms.value():
                mp.set_speed(0, +SPEED)
                wait_until(lambda: ms.value() < LINE_THRESHOLD)
                mp.stop()
