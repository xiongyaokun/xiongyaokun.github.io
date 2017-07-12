#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/2 9:45
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice40.py
# @Software: PyCharm

things = ['a', 'b', 'c', 'd']
print things[1]
things[1] = 'z'
print things

stuff = {'name':'Zed', 'age':26, 'height':6*12+2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = 'San Francisco'
print stuff
print stuff

stuff[1] = 'Wow'
stuff[2] = 'Neato'

# 每次添加新元素后，打印字典里的元素的顺序都不一样
print stuff

del stuff[1]
print stuff

cities = {'CA':'San Francisco', 'MI':'Detroit', 'FL':'Jackasonville'}
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found!"

# ok pay attention!
cities['_find'] = find_city
# print cities['_find']

while True:
    print "State?(Enter to quit)",
    state = raw_input('-->')
    if not state:
        break
    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    # city_found = find_city(cities,state)
    print city_found


for key,value in cities.items():
    print "%s : %s" %(key, value)