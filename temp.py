#!/usr/bin/env python

import time
import socket
import getpass
import requests

from gpiozero import CPUTemperature

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
    cpu = CPUTemperature()

    url = 'http://192.168.0.3:8280/Bean'
    my_app = 'temperature'
    log_level = 'DEBUG'
    hostname = get_name()
    ip_addr = get_ip()
    user = get_user()

    while True:
        my_msg = cpu.temperature
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
