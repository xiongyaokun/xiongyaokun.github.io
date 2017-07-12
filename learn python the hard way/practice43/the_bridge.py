#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 14:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : the_bridge.py
# @Software: PyCharm


def the_bridge():
    print '''
    You burst onto the Bridge with the neutron destruct bomb under your arm and surprises 5 Gothons who are trying to
    take control of the ship. Each of them has an even uglier clown costume than the last. They haven't pulled their
    weapons out yet, as they see the active bomb under your arm and don't want to set it off.'''
    action = raw_input("-->")

    if action == "throw the bomb":
        print "In a panic you throw the bomb at the group of Gothons and make a leap for the door. Right as you drop" \
              "it a Gothon shoots you right in the back killing you. As you die you see another Gothon frantically" \
              "try to disarm the bomb. You die knowing they will probably blow up when it goes off."
        return "death"
    elif action == "slowly place the bomb":
        print "You point your blaster at the bomb under your arm and the Gothons put their hands up and start to sweat." \
              "You inch backward to the door, open it, and then carefully place the bomb on the floor, pointing your blaster" \
              "at it. You then jump back through the door, punch the close button and blast the lock so the Gothons can't" \
              "get out. Now that the bomb is placed you run to te escapepod to get off this tin can."
        return "escape_pod"
    else:
        print "DOES NOT COMPUTE!"
        return "the_bridge"
