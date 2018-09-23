# Remote Servo Control
import requests


class RemoteServo(object):
    def __init__(self, pin=18, rotMin=0, rotMax=180, pulseMin=50, pulseMax=250):
        self.setup(pin, rotMin, rotMax, pulseMin, pulseMax)

    def send(self):
        # Here is where we will add the code to send the message to the ServoServer
        return

    def rotateTo(self, rotation):
        self.send(rotation)

    def sweep(self, rotFrom, rotTo, delay):
        self.rotateTo(rotFrom)
        step = 1
        if rotFrom > rotTo:
            step = -1
        for i in range(int(rotFrom), int(rotTo), step):
            self.rotateTo(i)
            time.sleep(delay)

def testRotate():
    myS = RemoteServo()
    myS.rotateTo(myS.rotMin)
    for i in range(myS.rotMin, myS.rotMax, 10):
        myS.rotateTo(i)

def testSweep():
    myS = RemoteServo()
    myS.sweep(0, 90, 0.1)
    myS.sweep(90, 0, 0.1)

if __name__ == '__main__':
    testSweep()
