#!/usr/bin/env python
#James Parks
#02/07/18

import os
import json

from bot import bot

class TankBot(bot.Bot):
    def __init__(self, config_path):
        super(TankBot, self).__init__(config_path)
        self.claw_state = 0
        self.headlight_state = 0
        return

    def forward(self):
        #Make both motors go forward
        return

    def backward(self):
        #Make both motors go backward
        return

    def left(self):
        #Make tank rotate left
        return

    def right(self):
        #make tank rotate right
        return

    def claw_close(self):
        #make claw close
        self.servos['claw_servo'].set_angle(0)
        self.claw_state(1)
        return

    def claw_open(self):
        #make claw open
        self.servos['claw_servo'].set_angle(90)
        self.claw_state(0)
        return

    def claw_toggle(self):
        #toggle the state of the claw
        if self.claw_state:
            self.claw_open()
        else:
            self.claw_close()
        return

    def light_on(self):
        #turn headlight on
        self.lights['headlight'].set_on()
        self.headlight_state = 1
        return

    def light_off(self):
        #turn headlight off
        self.lights['headlight'].set_off()
        self.headlight_state = 0
        return

    def light_toggle(self):
        #toggle the state of the headlight
        if self.headlight_state:
            self.light_off()
        else:
            self.light_on()
        return

    def claw_angle(self, angle):
        self.claw_servo.setAngle(angle)

    def calisthenics(self):
        #Run some tests and stretch our motors
        self.left(2)
        self.right(4)
        self.left(2)
        self.claw_close()
        self.claw_open()
        for i in range(12):
            self.light_toggle()
        self.light_off()
        return


