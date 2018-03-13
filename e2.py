from manoeuvres.centralizefront import centralizeFront as cf
from devices import driver, lineSensorArray

d = driver
lsa = lineSensorArray

def s():
	driver.stop()

def log():
	print(lineSensorArray.values(), lineSensorArray.line_pos)
