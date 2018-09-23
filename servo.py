# Servo Control
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 

class Servo(object):
    def __init__(self, pin=18, rotMin=0.0, rotMax=180.0, pulseMin=50.0, pulseMax=250.0):
        import wiringpi
        self.setup(pin, rotMin, rotMax, pulseMin, pulseMax)

    def setup(self, pin=18, rotMin=0.0, rotMax=180.0, pulseMin=50.0, pulseMax=250.0):
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

    def rotate(self, rotation):
        pulse = translate(rotation, self.rotMin, self.rotMax, self.pulseMin, self.pulseMax)
        wiringpi.pmWrite(self.pin, pulse)

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

