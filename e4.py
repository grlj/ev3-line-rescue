from devices import driver
import queue as queue

class Backtracker:

	tracker = queue.LifoQueue(maxsize=256)

	def insertion():
		position_tuple = driver.position()
		last_item = tracker.get()
		position_tuple[0] += last_item[0]
		position_tuple[1] += last_item[1]
		tracker.put(last_item)
		tracker.put(position_tuple)

	def read():
		last_item = tracker.get()
		semilast_item = tracker.get()
	return tuple([semilast_item[i] - last_item[i] for i in range(2)])
