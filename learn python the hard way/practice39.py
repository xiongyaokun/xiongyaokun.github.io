#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/27 0:22
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice39.py
# @Software: PyCharm
from string import join

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that lines, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding ...", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go ...", stuff

print "Let's do something with stuff."

print stuff[1]
print stuff[-1] # whoa1 fancy
print stuff.pop()
print ' '.join(stuff) # what? cool
print join(' ', stuff)
print '#'.join(stuff[3:5]) # super stellar!

# 'list' object has no attribute 'join'
# print stuff.join(' ') # wow!