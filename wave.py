import Servo

myS = Servo.Servo()

for i in range(0, 4):
    myS.sweep(60, 110, 0.01)
    myS.sweep(110, 60, 0.01)


