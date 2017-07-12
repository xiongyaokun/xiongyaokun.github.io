#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/4 8:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice11.py
# @Software: PyCharm

# 注意在print 末尾加上一个 ， 这样每打印一行不会立即跑到下一行
print 'How old are you?',
age = raw_input()
print 'How tall are you?',
height = raw_input()
print 'How much do you weigh?(kg)',
weight = raw_input()

print "So, you're %r old, %r tall and %r kg heavy." % (age, height, weight)
