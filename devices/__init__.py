from ev3dev.ev3 import ColorSensor, LightSensor
from .driver import Driver
from .linesensorarray import LineSensorArray


driver             = Driver('outA', 'outB')
lineSensorArray    = LineSensorArray('in1')
colorSensors       = (ColorSensor('mux1'), ColorSensor('mux2'))
centralLineSensor  = LightSensor('mux3')
