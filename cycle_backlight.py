#!/usr/bin/python3
#James Parks

# The Adafruit 2.8" TFT display (https://www.adafruit.com/product/2298) comes with buttons
# This assigns one of the buttons to cycle through backlight intensity settings

import RPi.GPIO as gpio
import time

class Cycler(object):
    def __init__(self):
        # set up variables
        self.switch_pin = 22
        self.out_pin = 18
        self.states_list = [1023, 768, 512, 128, 10, 0]
        self.duty_cycle_list = [100, 75, 50, 25, 10, 0]
        self.cur_state = 0
        self.VERBOSITY = 6 

        freq = 500
 
        # set up pins
        gpio.setmode(gpio.BCM)
        gpio.setup(self.switch_pin, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(self.out_pin, gpio.OUT)
        self.p = gpio.PWM(self.out_pin, freq)
        self.p.start(100)

        #cmd = 'gpio -g mode {} pwm; gpio pwmc 1000'.format(self.SWITCH_PIN)
        #status, output = commands.getstatusoutput(cmd)

    def _log(self, priority, msg):
        if priority >= self.VERBOSITY:
            print(msg)

    def run(self):
        button_press = gpio.input(self.switch_pin)
        if not button_press:
            self._log(1, 'button pressed')
            if self.cur_state >= len(self.states_list)-1:
                self.cur_state = 0
            else:
                self.cur_state += 1
            self.set_state(self.cur_state)

    def set_state(self, value):
        #gpio.output(self.out_pin, value)
        self.p.ChangeDutyCycle(self.duty_cycle_list[self.cur_state])
        #cmd = 'gpio -g {} {}'.format(self.SWITCH_PIN, value)
        #status, output = commands.getstatusoutput(cmd)
        self._log(1, 'current state: {}'.format(self.cur_state))
        time.sleep(0.5)

if __name__ == '__main__':
    myCycler = Cycler()
    while True:
        myCycler.run()
