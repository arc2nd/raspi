#!/usr/bin/env python

import sys
import Servo

myS = Servo.Servo()
sMax = 62
sMin = 10
rate = 0.025

if len(sys.argv) > 1:
    for i in range(0, int(sys.argv[1])):
        myS.sweep(sMin, sMax, rate)
        myS.sweep(sMax, sMin, rate)
else:
    myS.sweep(sMin, sMax, rate)
    myS.sweep(sMax, sMin, rate)


