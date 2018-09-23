#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore

class ServoSlider(QtGui.QWidget):
    def __init__(self, name='Servo', servo_obj=None, parent=None):
        super(ServoSlider, self).__init__()

        self.servo_obj = servo_obj
        layout = QtGui.QVBoxLayout()

        label_layout = QtGui.QHBoxLayout()
        label = QtGui.QLabel('{}:'.format(name))
        label_layout.addWidget(label)

        self.spin = QtGui.QSpinBox()
        self.spin.setKeyboardTracking(False)
        self.spin.setRange(0.0, 180.0)
        self.spin.setValue(90)
        label_layout.addWidget(self.spin)

        layout.addLayout(label_layout)

        self.slider = QtGui.QSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)
        self.slider.setValue(90)
        self.slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.slider.setTickInterval(30)
        layout.addWidget(self.slider)

        self.setLayout(layout)

        self.slider.valueChanged.connect(self.slider_val_changed)
        self.spin.valueChanged.connect(self.spin_val_changed)

        self.show()

    def slider_val_changed(self):
        position = self.slider.value()
        #self.servo_pos.setText(str(position))
        self.spin.setValue(position)
        if self.servo_obj:
            self.update_servo()

    def spin_val_changed(self):
        val = self.spin.value()
        self.slider.setValue(val)
        if self.servo_obj:
            self.update_servo()

    def getValue(self):
        val = self.spin.value()
        pos = self.slider.position()
        if val == pos:
            return self.spin.value()
        else:
            return 'Error: slider and spin box don\'t match'

    def update_servo(self):
        val = self.spin.value()
        pos = self.slider.position()
        if self.servo_obj:
            if val == pos:
                self.servo_obj.rotateTo(val)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #make the window 
    win = ServoSlider(name='Test Servo 1')
    sys.exit(app.exec_())



