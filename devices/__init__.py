from ev3dev.ev3 import ColorSensor, Motor
from .driver import Driver
from .linesensorarray import LineSensorArray
from .colorsensor import ColorSensor


driver              = Driver('outA', 'outB')
arm                 = Motor('outD')
claws               = Motor('outC')
line_sensor_array   = LineSensorArray('in1')
color_sensors       = (ColorSensor('mux3'), ColorSensor('mux1'))
central_line_sensor = LightSensor('mux2')
