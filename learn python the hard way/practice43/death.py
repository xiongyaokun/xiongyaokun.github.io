#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 14:48
# @Author  : xiongyaokun
# @Site    : 
# @File    : death.py
# @Software: PyCharm
from random import randint


def death():
    quips = ["You died. You kinda suck at this.",
             "Nice job, you died ...jackass.",
             "Such a loser.",
             "I have a small puppy that's better at this."]
    print quips[randint(0, len(quips)-1)]
    exit(1)