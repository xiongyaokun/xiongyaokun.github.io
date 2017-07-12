#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/11 15:11
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice32.py
# @Software: PyCharm

hairs = ['brown', 'blond', 'red']
eyes = ['brown', 'blue', 'green']
weights = [1, 2, 3, 4]

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kind of for-loop goes through a lise
for number in the_count:
    print "This is count %d" % number

# some as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    # num = i
    elements.append('element' + str(i))

# Now we can print them out too
for i in elements:
    print "Elements was：%s" % i
