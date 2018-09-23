#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore

class OnOffButton(QtGui.QWidget):
    def __init__(self, name='Object', obj=None, parent=None):
        super(OnOffButton, self).__init__()

        self.obj = obj
        layout = QtGui.QVBoxLayout()

        label_layout = QtGui.QHBoxLayout()
        label = QtGui.QLabel('{}:'.format(name))
        label_layout.addWidget(label)

        self.button = QtGui.QPushButton('off')
        self.button.setStyleSheet('background-color: #cccccc')
        self.button.setCheckable(True)
        label_layout.addWidget(self.button)

        layout.addLayout(label_layout)

        self.setLayout(layout)

        self.button.clicked.connect(self.button_val_changed)

        self.show()

    def button_val_changed(self):
        if self.button.isChecked():
            self.button.setText('ON')
            self.button.setStyleSheet("background-color: yellow")
        else:
            self.button.setText('OFF')
            self.button.setStyleSheet('background-color: #cccccc')
        return self.button.isChecked()

    def getValue(self):
        return self.button.isChecked()    


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #make the window 
    win = OnOffButton(name='Test Button 1')
    sys.exit(app.exec_())



