#!/usr/bin/env python
import sys

import Servo

times = sys.argv[1]
myS = Servo.Servo()

for i in range(0, int(times)):
    myS.sweep(60, 120, 0.01)
    myS.sweep(120, 60, 0.01)


