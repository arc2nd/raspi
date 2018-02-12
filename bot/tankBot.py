#!/usr/bin/env python
#James Parks
#02/07/18

import os
import json
import time

from bot import bot

class TankBot(bot.Bot):
    def __init__(self, config_path):
        super(TankBot, self).__init__(config_path)
        self.claw_state = 0.0
        self.head_light_state = 0
        return

    def forward(self, duration=1000, speed=1):
        #Make both motors go forward
        self.motors['left_motor'].forward(duration, speed)
        self.motors['right_motor'].forward(duraton, speed)
        return

    def backward(self, duration=1000, speed=1):
        #Make both motors go backward
        self.motors['left_motor'].backward(duration, speed)
        self.motors['right_motor'].backward(duration, speed)
        return

    def left(self, duration=1000, speed=1):
        #Make tank rotate left
        #right motor forward
        #left motor backward
        self.motors['left_motor'].backward(duration, speed)
        self.motors['right_motor'].forward(duration, speed)
        return

    def right(self, duration=1000, speed=1):
        #make tank rotate right
        #right motor backward
        #left motor forward
        self.motors['left_motor'].forward(duration, speed)
        self.motors['right_motor'].backward(duration, speed)
        return

    def claw_close(self):
        #make claw close
        self.claw_angle(90)
        self.claw_state = 1.0
        return

    def claw_open(self):
        #make claw open
        self.claw_angle(0)
        self.claw_state = 0.0
        return

    def claw_angle(self, angle):
        self.servos['claw_servo'].set_angle(angle)
        self.claw_state = float(angle)/90.0

    def claw_toggle(self):
        #toggle the state of the claw
        if self.claw_state:
            self.claw_open()
        else:
            self.claw_close()
        return

    def light_on(self):
        #turn headlight on
        self.lights['head_light'].set_on()
        self.head_light_state = 1
        return

    def light_off(self):
        #turn headlight off
        self.lights['head_light'].set_off()
        self.head_light_state = 0
        return

    def light_toggle(self):
        #toggle the state of the headlight
        if self.head_light_state:
            self.light_off()
        else:
            self.light_on()
        return

    def delay(pause=15)
        time.sleep(pause)

    def calisthenics(self):
        #Run some tests and stretch our motors
        self.left(2000)
        self.delay()
        self.right(4000)
        self.delay()
        self.left(2000)
        self.delay()
        self.claw_close()
        self.delay()
        self.claw_open()
        self.delay()
        for i in range(0,95,5):
            self.claw_angle(i)
            self.delay()
        self.claw_open()
        for i in range(12):
            self.light_toggle()
            self.delay()
        self.light_off()
        return


