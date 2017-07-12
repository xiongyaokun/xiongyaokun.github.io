#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 14:33
# @Author  : xiongyaokun
# @Site    : 
# @File    : main_start.py
# @Software: PyCharm

from central_corridor import central_corridor
from escape_pod import escape_pod
from laser_weapon_armory import laser_weapon_armory
from the_bridge import the_bridge
from death import death

ROOMS = {
    'death': death,
    'central_corridor': central_corridor,
    'laser_weapon_armory': laser_weapon_armory,
    'the_bridge': the_bridge,
    'escape_pod': escape_pod
}

def runner(map, start):
    next = start

    while True:
        room = map[next]
        print "\n--------"
        next = room()

runner(ROOMS, 'central_corridor')