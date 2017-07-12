#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/4 0:21
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice8.py
# @Software: PyCharm

formatter = '%r %r %r %r'

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'four')
print formatter % (False, True, True, False)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it did't sing.",
    "So I said goodnight."
)