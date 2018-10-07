#!/usr/bin/env python

import sys
import Servo

myS = Servo.Servo()

if len(sys.argv) > 1:
    for i in range(0, sys.argv[1]):
        myS.sweep(60, 120, 0.01)
        myS.sweep(120, 60, 0.01)
else:
    myS.sweep(0, 174, 0.001)


