from providers.distancemeterproviders import front_distance_meter as fdm
from providers.robotsizeprovider import distance_to_motor_rot as dtmr 
from providers.motorpairprovider import motor_pair as mp
from lib.machinestate import MachineState

if FDM.value() < 10:
	mp.stop()
