from ev3dev.ev3 import Motor

class MotorPair:
    def __init__(self, left_motor_port, right_motor_port):
        self.left  = Motor(left_motor_port)
        self.right = Motor(right_motor_port)

    @property
    def max_speed(self):
        return max(self.left.max_speed, self.right.max_speed)

    def set_speed(self, forward=0, turning=0):
        self.left.run_forever(speed_sp=forward + turning)
        self.right.run_forever(speed_sp=forward - turning)

    def stop(self):
        self.set_speed(0)
        self.left.run_to_rel_pos(position_sp=0, speed_sp=100)
        self.right.run_to_rel_pos(position_sp=0, speed_sp=100)

    def run_to_lr(self, left, right, speed):
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

    def reset(self):
        self.left.reset()
        self.right.reset()
