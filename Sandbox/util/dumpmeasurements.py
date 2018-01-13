from lib.measurements import measurements
import json

def save_dump(path='measurements/default_dump.json'):
	with open(path, 'w') as fp:
	    json.dump(measurements, fp)
