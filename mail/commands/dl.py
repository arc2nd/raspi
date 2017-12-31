#!/usr/bin/python

import commands

def dl(url):
    print('DL: {}'.format(url))
    cmd = 'python /home/<user>/scripts/convertToAudio.py -u {}'.format(url)
    print('cmd: {}'.format(url))
    status, output = commands.getstatusoutput(cmd)
    print('Status: {}'.format(status))
    print('Output: {}'.format(output))

