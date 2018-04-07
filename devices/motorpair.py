from ev3dev.ev3 import Motor

class MotorPair:
    def __init__(self, left_motor_port, right_motor_port):
        self.left  = Motor(left_motor_port)
        self.right = Motor(right_motor_port)

    @property
    def max_ticks_per_second(self):
        return max(self.left.max_speed, self.right.max_speed)

    @property
    def max_speed(self):
        return self.max_ticks_per_second

    def set_speed(self, forward=0, turning=0):
        self.left.run_forever(speed_sp=bounded(forward + turning, self.max_ticks_per_second))
        self.right.run_forever(speed_sp=bounded(forward - turning, self.max_ticks_per_second))
        return self

    def stop(self):
        self.set_speed(0)
        self.left.run_to_rel_pos(position_sp=0, speed_sp=100)
        self.right.run_to_rel_pos(position_sp=0, speed_sp=100)
        return self

    def run_to_lr(self, left, right, speed):
        left_speed = speed if left >= right else speed * (left / right)
        right_speed = speed if right >= left else speed * (right / left)
        self.left.run_to_rel_pos(position_sp=left, speed_sp=left_speed)
        self.right.run_to_rel_pos(position_sp=right, speed_sp=right_speed)
        self.wait()
        return self

    @property
    def position(self):
        return self.left.position, self.right.position


    def block(self):
        while self.running():
            pass
        return self

    def wait(self):
        return self.block()

    def running(self):
        return 'running' in self.left.state + self.right.state

    def reset(self):
        self.left.reset()
        self.right.reset()
        return self

    @property
    def stop_action(self):
        return self.left.stop_action

    @stop_action.setter
    def stop_action(self, value):
        self.left.stop_action = value
        self.right.stop_action = value

    def skip(self, speed=100):
        if (speed > 0):
            self.left.run_to_rel_pos(position_sp=1, speed_sp=speed)
            self.right.run_to_rel_pos(position_sp=-1, speed_sp=speed)
        else:
            self.left.run_to_rel_pos(position_sp=-1, speed_sp=speed)
            self.right.run_to_rel_pos(position_sp=1, speed_sp=speed)
        return self

def bounded(x, max_abs):
    return max(-max_abs, min(x, max_abs))
