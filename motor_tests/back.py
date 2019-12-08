#!/usr/bin/env python

# Import required modules
import time
import RPi.GPIO as GPIO

"""
STBY = Pin 13 (GPIO #21) blue

Motor A:
PWMA = Pin 7 (GPIO #4) white
AIN2 = Pin 11 (GPIO #17) yellow
AIN1 = Pin 12 (GPIO #18) orange

Motor B:
BIN1 = Pin 15 (GPIO #22) green/teal
BIN2 = Pin 16 (GPIO #23) brown
PWMB = Pin 18 (GPIO #24) purple
"""

"""
####################
wiringPi alternative:
####################

int softPwmCreate (int pin, int initialValue, int pwmRange) 
void softPwmWrite (int pin, int value) 

import wiringpi

OUTPUT = 1

PIN_TO_PWM = 1

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_PWM, OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM, 0, 100) # Setup PWM using Pin, Initial Value and Range parameters

for time in range(0,4):
    for brightness in range(0, 100): # Going from 0 to 100 will give us full off to full on
        wiringpi.softPwmWrite(PIN_TO_PWM, brightness) # Change PWM duty cycle
        wiringpi.delay(10) # Delay for 0.2 seconds
    for brightness in reversed(range(0, 100)):
        wiringpi.softPwmWrite(PIN_TO_PWM, brightness)
        wiringpi.delay(10)
"""

# Pin constants
PWMA = 7
AIN1 = 12
AIN2 = 11
PWMB = 18
BIN1 = 15
BIN2 = 16
STBY = 13

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# set up GPIO pins
GPIO.setup(PWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(AIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(AIN1, GPIO.OUT) # Connected to AIN1
GPIO.setup(STBY, GPIO.OUT) # Connected to STBY
GPIO.setup(BIN1, GPIO.OUT) # Connected to BIN1
GPIO.setup(BIN2, GPIO.OUT) # Connected to BIN2
GPIO.setup(PWMB, GPIO.OUT) # Connected to PWMB

GPIO.output(STBY, GPIO.HIGH)

# Drive the motor counterclockwise
# Motor A:
GPIO.output(AIN1, GPIO.HIGH) # Set AIN1
GPIO.output(AIN2, GPIO.LOW) # Set AIN2
# Motor B:
GPIO.output(BIN1, GPIO.HIGH) # Set BIN1
GPIO.output(BIN2, GPIO.LOW) # Set BIN2

# Set the motor speed
# Motor A:
GPIO.output(PWMA, GPIO.HIGH) # Set PWMA
# Motor B:
GPIO.output(PWMB, GPIO.HIGH) # Set PWMB

# Disable STBY (standby)
GPIO.output(STBY, GPIO.HIGH)

# Wait x seconds
time.sleep(2)

# Reset all the GPIO pins by setting them to LOW
GPIO.output(AIN1, GPIO.LOW) # Set AIN1
GPIO.output(AIN2, GPIO.LOW) # Set AIN2
GPIO.output(PWMA, GPIO.LOW) # Set PWMA
GPIO.output(STBY, GPIO.LOW) # Set STBY
GPIO.output(BIN1, GPIO.LOW) # Set BIN1
GPIO.output(BIN2, GPIO.LOW) # Set BIN2
GPIO.output(PWMB, GPIO.LOW) # Set PWMB
