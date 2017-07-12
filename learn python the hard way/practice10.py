#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/4 8:11
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice10.py
# @Software: PyCharm

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
slim_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print slim_cat

# %r 打印的是脚本里的原文
print 'I said: %r' % slim_cat
# %s打印的是最终希望显示的格式
print 'I said: %s' % slim_cat