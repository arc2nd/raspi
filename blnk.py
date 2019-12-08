#!/usr/bin/env python

import sys
import time
import RPi.GPIO as gp

gp.setmode(gp.BOARD)

pin_list = [7,11,12,13,15,16]

def blink(pin):
    for x in range(1):
        gp.output(pin, gp.HIGH)
        time.sleep(0.25)
        gp.output(pin, gp.LOW)
        time.sleep(0.1)

if len(sys.argv) > 1:
    pin = int(sys.argv[1])
    gp.setup(pin, gp.OUT)
    for x in range(15):
        blink(pin)
        time.sleep(0.1)
else:
    for x in range(15):
        for p in pin_list:
            gp.setup(p, gp.OUT)
            blink(p)


gp.cleanup()
