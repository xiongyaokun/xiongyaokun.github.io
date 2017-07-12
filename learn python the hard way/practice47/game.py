#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 22:27
# @Author  : xiongyaokun
# @Site    : 
# @File    : game.py
# @Software: PyCharm

class Room(object):


    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        # update()方法把括号内的字典的键/值对，更新到调用者字典中
        self.paths.update(paths)

