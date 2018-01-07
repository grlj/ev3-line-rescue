from importlib import reload
from util import robotutils
from providers import motorpairprovider, linesensortripletprovider
from states import sharpturnstate
from devices import motorpair
from entrypoints import test1


def refresh():
	to_reload = [robotutils, motorpair, motorpairprovider, sharpturnstate]
	for p in to_reload:
		reload(p)

	global mp, lm, rm, ls, stop, STS

	mp = motorpairprovider.motor_pair
	lm = mp.left
	rm = mp.right

	ls = linesensortripletprovider.line_sensors

	stop = robotutils.stop_motors

	sts = sharpturnstate
	STS = sts.SharpTurnState

refresh()
