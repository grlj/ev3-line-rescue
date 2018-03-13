from .motorpair import MotorPair
from robotspecs import robot_specs as rs
from util.conversions import distance_to_motor as dtm, motor_to_distance as mtd

wr = rs['wheel radius']
a  = rs['axle length']


class Driver(MotorPair):
    @property
    def max_speed(self):  # override
        return mtd(super().max_speed, wr)

    # [cm/s]
    def set_speed(self, forward=0, turning=0):  # override
        super().set_speed(dtm(forward, wr), dtm(turning,  wr))

    # def set_steering() TODO

    # [cm], [cm], [cm/s]
    def run_to_lr(self, left, right, speed):  # override
        super().run_to_lr(dtm(left, wr), dtm(right, wr), dtm(speed, wr))

    def lr(self, left, right, speed):
        self.run_to_lr(left, right, speed)
