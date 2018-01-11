from providers.distancemeterprovider import front_distance_meter as fdm
from providers.robotsizeprovider import distance_to_motor_rot as ditmr
from providers.robotsizeprovider import deg_to_motorpair_deg as detmd 
from providers.motorpairprovider import motor_pair as mp
from lib.machinestate import MachineState

THRESHOLD = 10
SPEED = 200
RIGHT_ANGLE = 90 #in deg
FOWARD_MOVEMENT_PERPENDICULAR = 10 #in cm
FOWARD_MOVEMENT_PARALLEL = 10 #in cm

class EvasionState(MachineState):
	def run(self):
		while True:
			print(fdm.value())
			if fdm.value() < THRESHOLD:
				mp.stop()
				mp.block()
				mp.reset()
				mp.run_to_lr(-detmd(RIGHT_ANGLE), detmd(RIGHT_ANGLE), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(ditmr(FOWARD_MOVEMENT_PERPENDICULAR), ditmr(FOWARD_MOVEMENT_PERPENDICULAR), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(detmd(RIGHT_ANGLE), -detmd(RIGHT_ANGLE), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(ditmr(FOWARD_MOVEMENT_PARALLEL), ditmr(FOWARD_MOVEMENT_PARALLEL), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(ditmr(FOWARD_MOVEMENT_PARALLEL), ditmr(FOWARD_MOVEMENT_PARALLEL), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(ditmr(FOWARD_MOVEMENT_PERPENDICULAR), ditmr(FOWARD_MOVEMENT_PERPENDICULAR), SPEED)
				mp.block()
				mp.reset()
				mp.run_to_lr(-detmd(RIGHT_ANGLE), detmd(RIGHT_ANGLE), SPEED)
				mp.block()
				mp.reset()
