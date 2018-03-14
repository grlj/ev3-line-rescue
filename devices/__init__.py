from ev3dev.ev3 import LightSensor
from .driver import Driver
from .linesensorarray import LineSensorArray
from .colorsensor import ColorSensor

driver              = Driver('outA', 'outB')
line_sensor_array   = LineSensorArray('in1')
color_sensors       = (ColorSensor('mux3'), ColorSensor('mux1'))
central_line_sensor = LightSensor('mux2')
