from .motorpair import MotorPair
from robotspecs import robot_specs as rs
from util.conversions import distance_to_motor as dtm, motor_to_distance as mtd

wr = rs['wheel radius']
a  = rs['axle length']


class Driver(MotorPair):
    @property
    def max_speed(self):
        return mtd(super().max_speed)

    # [cm/s]
    def set_speed(self, forward=0, turning=0):
        return super().set_speed(dtm(forward), dtm(turning))

    # def set_steering() TODO

    # [cm], [cm], [cm/s]
    def run_to_lr(self, left, right, speed):
        return super().run_to_lr(dtm(left), dtm(right), dtm(speed))

    def lr(self, left, right, speed):
        return self.run_to_lr(left, right, speed)        

    @property
    def position(self):
        return tuple([mtd(p) for p in super().position])

    @property
    def average_position(self):
        return sum(self.position) / 2