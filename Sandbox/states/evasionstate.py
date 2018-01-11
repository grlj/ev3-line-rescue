from providers.distancemeterproviders import front_distance_meter as fdm
from providers.robotsizeprovider import distance_to_motor_rot as ditmr
from providers.robotsizeprovider import deg_to_motorpair_deg as detmd 
from providers.motorpairprovider import motor_pair as mp
from lib.machinestate import MachineState

THRESHOLD = 10
SPEED = 200
RIGHT_ANGLE = 90
FOWARD_MOVEMENT_PARAREL = 10
FOWARD_MOVEMENT_PERPENDICULAR = 10

class EvasionState(MachineState):
	def run(self):
		while 1:
			if FDM.value() < THRESHOLD:
				mp.stop()
				mp.run_to_rel_pos(0, SPEED, detmd(RIGHT_ANGLE))
				mp.stop()
				mp.run_to_rel_pos(SPEED, 0, ditmr(FOWARD_MOVEMENT_PARAREL))
				mp.stop()
				mp.run_to_rel_pos(0, SPEED, -detmd(RIGHT_ANGLE))
				mp.stop()
				mp.run_to_rel_pos(SPEED, 0, ditmr(FOWARD_MOVEMENT_PERPENDICULAR))
				mp.stop()
				mp.run_to_rel_pos(0, SPEED, -detmd(RIGHT_ANGLE))
				mp.stop()
				mp.run_to_rel_pos(SPEED, 0, ditmr(FOWARD_MOVEMENT_PARAREL))
				mp.stop()
				mp.run_to_rel_pos(0, SPEED, detmd(RIGHT_ANGLE))
				mp.stop()
