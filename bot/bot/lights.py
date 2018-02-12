#!/usr/bin/python
#James Parks
#02/07/18


class Light(object):
    def __init__(self, pin):
        self.pin = pin
        self.state = 0
        return

    def light_on(self):
        print('turning light on')
        return

    def light_off(self):
        print('turning light off')
        return
