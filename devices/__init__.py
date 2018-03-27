from ev3dev.ev3 import ColorSensor, Motor
from .driver import Driver
from .linesensorarray import LineSensorArray
from .colorsensor import ColorSensor


driver              = Driver('outA', 'outB')
arm                 = Motor('outC')
claws               = Motor('outD')
line_sensor_array   = LineSensorArray('in1')
color_sensors       = (ColorSensor('in2'), ColorSensor('in3'))
# central_line_sensor = ColorSensor('in4')
