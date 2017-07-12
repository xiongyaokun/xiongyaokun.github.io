#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/4 10:24
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice15.py
# @Software: PyCharm

from sys import argv

script, filename = argv

txt = open(filename)
print "Here's your file %r:" % filename
print txt.read()
txt.close()
print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)
print txt_again.read()
txt_again.close()