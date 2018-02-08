#!/usr/bin/python3
#James Parks
#02/07/18

import os
import json

import bot.servos as servos
import bot.motors as motors
import bot.lights as lights
import bot.sensors as sensors


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
                if 'servo' in item.lower():
                    self.servos[item] = servos.Servo(self.config_dict[item])
                if 'motor' in item.lower():
                    self.motors[item] = motors.Motor(self.config_dict[item])
                if 'light' in item.lower():
                    self.lights[item] = lights.Light(self.config_dict[item])
                if 'sensor' in item.lower():
                    self.sensors[item] = sensors.Sensor(self.config_dict[item])

        return

