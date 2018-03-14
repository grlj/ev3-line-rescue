from ev3dev.ev3 import ColorSensor, LightSensor
from .driver import Driver
from .linesensorarray import LineSensorArray


driver              = Driver('outA', 'outB')
line_sensor_array   = LineSensorArray('in1')
colorSensors        = (ColorSensor('mux1'), ColorSensor('mux2'))
central_line_sensor = LightSensor('mux3')
