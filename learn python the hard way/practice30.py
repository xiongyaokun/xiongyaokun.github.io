#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/11 12:17
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice30.py
# @Software: PyCharm

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should't take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."


if people < cars and people > buses:
    print "Ok, let's take the cars."
elif people < cars and people < buses:
    print "Ok, let's take the cars and the buses."
else:
    print "Ok, let's take the buses."
