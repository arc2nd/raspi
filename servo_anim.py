#!/usr/bin/env python

import os
import json

def read_servo_anim(anim_file):
    anim_list = []
    with open(anim_file, 'r') as fp:
        anim_list = json.read(fp)
    return anim_list

def write_servo_anim(anim_file, anim_list):
    with open(anim_file, 'w') as fp:
        json.dump(anim_list, fp, indent=4, sort_keys=True)
    return os.path.exists(anim_file)
