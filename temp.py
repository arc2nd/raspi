#!/usr/bin/env python

import os
import time
import socket
import getpass
import requests
import commands

global GENCMD
try:
    from gpiozero import CPUTemperature
    GENCMD = False
except:
    GENCMD = True


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 53))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        print('Couldn\'t connect to determine IP address')
        return None

def get_name():
    try:
        response = socket.getfqdn()
        hostname = response.split('.')[0]
        return hostname
    except:
        print('Couldn\'t determine machine hostname')
        return None

def get_user():
    try:
        user = getpass.getuser()
        return user
    except:
        print('Couldn\'t determine user')
        return None


def send_temp():
    global GENCMD
    if not GENCMD:
        try:
            cpu = CPUTemperature()
        except:
            GENCMD = True

    url = 'http://192.168.0.3:8280/Bean'
    my_app = 'temperature'
    log_level = 'DEBUG'
    hostname = get_name()
    ip_addr = get_ip()
    user = get_user()

    while True:
        if not GENCMD:
            my_msg = cpu.temperature
        else:
            if os.path.exists('/opt/vc/bin/vcgencmd'):
                my_msg = commands.getoutput('/opt/vc/bin/vcgencmd measure_temp').split('=')[-1].split("'C")[0]
            else:
                print('Can\'t log temp')
        data_dict = {'app': my_app, 
                     'level': log_level, 
                     'hostname': hostname, 
                     'ip': ip_addr, 
                     'user': user, 
                     'msg': my_msg}
        resp = requests.post(url, data_dict)
        print('logged temp at: {}'.format(my_msg))
        time.sleep(600)

if __name__ == '__main__':
    send_temp()
