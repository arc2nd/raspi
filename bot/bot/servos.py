#!/usr/bin/python
#James Parks
#02/07/18


class Servo(object):
    def __init__(self, pin):
        self.pin = pin
        self.angle = 45
        return

    def set_angle(self, angle):
        print('setting angle to: {}'.format(angle))
        return
