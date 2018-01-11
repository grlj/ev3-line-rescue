from ev3dev.ev3 import Motor


class MotorPair:
    def __init__(self, left: Motor, right: Motor):
        self.left = left
        self.right = right

    def set_speed(self, forward, turning=0): #run at set speed or turn with both motors
        self.left.run_forever(speed_sp=forward + turning)
        self.right.run_forever(speed_sp=forward - turning)

    def run_to_rel_pos(self, forward, turning=0, pos=0): #run to left motor rot relative to current pos
        start_pos = self.left.position
        self.set_speed(forward, turning)
        while abs(self.left.position - start_pos) < pos:
            pass
        self.stop()

    def stop(self): #stop motorpair
        self.set_speed(0)
        self.left.run_to_rel_pos(position_sp=0, speed_sp=100)
        self.right.run_to_rel_pos(position_sp=0, speed_sp=100)

    def run_to_lr(self, left, right, speed): #run untill both motors simultaneously reach set motor rot
        lrel = abs(left - self.left.position)
        rrel = abs(right - self.right.position)
        left_speed = speed if lrel >= rrel else speed * (lrel / rrel)
        right_speed = speed if rrel >= lrel else speed * (rrel / lrel)
        self.left.run_to_abs_pos(position_sp=left, speed_sp=left_speed)
        self.right.run_to_abs_pos(position_sp=right, speed_sp=right_speed)

    def block(self):
        while self.running():
            pass

    def running(self):
        return 'running' in self.left.state + self.right.state

    def reset(self): #reset motor state
        self.left.reset()
        self.right.reset()
