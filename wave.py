#!/usr/bin/env python

import Servo

myS = Servo.Servo()

for i in range(0, 4):
    myS.sweep(60, 120, 0.01)
    myS.sweep(120, 60, 0.01)


