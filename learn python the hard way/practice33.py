#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/17 18:09
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice33.py
# @Software: PyCharm

i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now:",numbers
    print "At the bottom i is %d" % i

print "The numbers is:"

for num in numbers:
    print num

def test(max, step):
    numbers1 = []
    i = 0
    while i < max:
        numbers1.append(i)
        print "Numbers now:", numbers1
        i = i + step

test(20,2)