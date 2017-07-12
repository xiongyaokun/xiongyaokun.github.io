#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/3 15:51
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice42.py
# @Software: PyCharm

class TheThing(object):

    def __init__(self):
        self.number = 0

    def someFunction(self):
        print "I got called!"

    def add_me_up(self, number):
        self.number += number
        return self.number

a = TheThing()
b = TheThing()
print type(a)
print type(b)
print "a is b",a is b

a.someFunction()
b.someFunction()

print a.add_me_up(10)
print a.add_me_up(5)
print a.number

print b.add_me_up(6)
print b.add_me_up(12)
print b.number