#!/usr/bin/python
#James Parks
#02/07/18

import os
import json

import servos
import motors
import lights
import sensors


class Bot(object):
    def __init__(self, config_path):
        self.config_dict = {}
        self.read_config(config_path)
        return

    def read_config(self, config_path=None):
        if os.path.exists(config_path):
            with open(config_path, 'r') as fp: 
                self.config_dict = json.load(fp)
        else:
            self.config_dict = {}

        self.servos = {}
        self.motors = {}
        self.lights = {}
        self.sensors = {}

        for item in self.config_dict:
            if 'pin' in item.lower():
                name = item.strip('_pin')
                if 'servo' in item.lower():
                    self.servos[name] = servos.Servo(self.config_dict[item])
                if 'motor' in item.lower():
                    self.motors[name] = motors.Motor(self.config_dict[item])
                if 'light' in item.lower():
                    self.lights[name] = lights.Light(self.config_dict[item])
                if 'sensor' in item.lower():
                    self.sensors[name] = sensors.Sensor(self.config_dict[item])

        return

    def inventory(self):
        print('Servos:')
        for item in self.servos:
            print('\t{}'.format(item))
        print('Motors:')
        for item in self.motors:
            print('\t{}'.format(item))
        print('Lights:')
        for item in self.lights:
            print('\t{}'.format(item))
        print('Sensors:')
        for item in self.sensors:
            print('\t{}'.format(item))

