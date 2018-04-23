from ev3dev.ev3 import ColorSensor, Motor, UltrasonicSensor
from .driver import Driver
from .linesensorarray import LineSensorArray
from .colorsensor import ColorSensor


driver              = Driver('outA', 'outB')
arm                 = Motor('outC')
claws               = Motor('outD')
line_sensor_array   = LineSensorArray('in1', inverted=False)
color_sensors       = (ColorSensor('in2'), ColorSensor('in3'))
ultrasonic_sensor   = UltrasonicSensor('in4')
# central_line_sensor = ColorSensor('in4')
