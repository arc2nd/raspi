#!/usr/bin/env python

import sys
import time
import RPi.GPIO as gp

gp.setmode(gp.BOARD)

pin_list = [7,11,12,13,15,16]

def blink(pin):
    for x in range(5):
        gp.output(pin, gp.HIGH)
        time.sleep(1)
        gp.output(pin, gp.LOW)
        time.sleep(0.5)

if len(sys.argv) > 1:
    pin = int(sys.argv[1])
    gp.setup(pin, gp.OUT)
    blink(pin)
else:
    for p in pin_list:
        gp.setup(p, gp.OUT)
        blink(p)


gp.cleanup()
