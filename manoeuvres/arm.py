from devices import arm, claws

def reset_arm():
	arm.reset()
	claws.reset()


def grab():
	arm.stop_action = 'hold'
	claws.stop_action = 'hold'
	arm.run_to_abs_pos(position_sp=95, speed_sp=100)
	while 'running' in arm.state:
		pass
	claws.run_to_abs_pos(position_sp=230, speed_sp=200)
	while 'running' in claws.state:
		pass
	arm.run_to_abs_pos(position_sp=125, speed_sp=100)
	claws.run_to_abs_pos(position_sp=0, speed_sp=300)
	while 'running' in claws.state:
		pass
	arm.run_to_abs_pos(position_sp=80, speed_sp=200)

def release():
	arm.stop_action = 'hold'
	claws.stop_action = 'hold'
	claws.run_to_abs_pos(position_sp=230, speed_sp=200)
	while 'running' in claws.state:
		pass
	claws.run_to_abs_pos(position_sp=0, speed_sp=200)
	arm.run_to_abs_pos(position_sp=0, speed_sp=100)
