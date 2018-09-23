# Local Servo Control
import requests
import Servo

class LocalServo(object):
    def __init__(self, pin=18, rotMin=0, rotMax=180, pulseMin=50, pulseMax=250):
        self.setup(pin, rotMin, rotMax, pulseMin, pulseMax)


    def receive(self):
        # Here is where we will add the code to receive commands from RemoteServo
        # and then interprate and execute them
        return

    def setup(self, pin=18, rotMin=0, rotMax=180, pulseMin=50, pulseMax=250):
        self.pin = pin
        self.rotMin = rotMin
        self.rotMax = rotMax
        self.pulseMin = pulseMin
        self.pulseMax = pulseMax

        self.servo = Servo.Servo(self.pin, self.rotMin, self.rotMax, self.pulseMin, self.pusleMax)

    def rotateTo(self, rotation):
        self.servo.rotateTo(rotation)

    def sweep(self, rotFrom, rotTo, delay):
        self.servo.sweep(rotFrom, rotTo, delay)


def testRotate():
    myS = LocalServo()
    myS.rotateTo(myS.rotMin)
    for i in range(myS.rotMin, myS.rotMax, 10):
        myS.rotateTo(i)

def testSweep():
    myS = LocalServo()
    myS.sweep(0, 90, 0.1)
    myS.sweep(90, 0, 0.1)

if __name__ == '__main__':
    testSweep()
