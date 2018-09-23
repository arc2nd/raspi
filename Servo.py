# Servo Control
import time 
import wiringpi


class Servo(object):
    def __init__(self, pin=18, rotMin=0, rotMax=180, pulseMin=50, pulseMax=250):
        self.setup(pin, rotMin, rotMax, pulseMin, pulseMax)

    def setup(self, pin=18, rotMin=0, rotMax=180, pulseMin=50, pulseMax=250):
        self.pin = pin
        self.rotMin = rotMin
        self.rotMax = rotMax
        self.pulseMin = pulseMin
        self.pulseMax = pulseMax
        # use 'GPIO naming'
        wiringpi.wiringPiSetupGpio()
        # set pin to be PWM output
        wiringpi.pinMode(self.pin, wiringpi.GPIO.PWM_OUTPUT)
        # set the PWM mode to milliseconds stype
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        # divide down clock
        wiringpi.pwmSetClock(192)
        wiringpi.pwmSetRange(2000)

    def rotateTo(self, rotation):
        pulse = translate(rotation, self.rotMin, self.rotMax, self.pulseMin, self.pulseMax)
        wiringpi.pwmWrite(int(self.pin), int(pulse))

    def sweep(self, rotFrom, rotTo, delay):
        self.rotateTo(rotFrom)
        step = 1
        if rotFrom > rotTo:
            step = -1
        for i in range(int(rotFrom), int(rotTo), step):
            self.rotateTo(i)
            time.sleep(delay)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)


def testRotate():
    myS = Servo()
    myS.rotateTo(myS.rotMin)
    for i in range(myS.rotMin, myS.rotMax, 10):
        myS.rotateTo(i)

def testSweep():
    myS = Servo()
    myS.sweep(0, 90, 0.1)
    myS.sweep(90, 0, 0.1)

if __name__ == '__main__':
    testSweep()
