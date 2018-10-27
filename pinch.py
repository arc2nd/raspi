#!/usr/bin/env python

import sys
import Servo

myS = Servo.Servo()

if len(sys.argv) > 1:
    for i in range(0, int(sys.argv[1])):
        myS.sweep(12, 52, 0.025)
        myS.sweep(52, 12, 0.025)
else:
    myS.sweep(12, 42, 0.025)
    myS.sweep(42, 12, 0.025)


