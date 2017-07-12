#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/8 11:26
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice21.py
# @Software: PyCharm

def add(a, b):
    print "Adding %d + %d" %(a, b)
    return a + b

def subtract(a, b):
    print "Subtract %d - %d" %(a, b)
    return a - b

def multiply(a, b):
    print "Multiply %d * %d" %(a, b)
    return a * b

def divide(a, b):
    print "Divide %d / %d" %(a, b)
    return a / b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, height: %d, weight: %d, iq: %d" %(age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.

print "Here is a puzzle"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes:", what, "， Can you do it by hand?"