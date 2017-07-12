#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/3 21:02
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice4.py
# @Software: PyCharm

# the total number of cars
cars = 100
# total seats in a car
space_in_a_car = 4.0
# total drivers
drivers = 30
# total passengers
passengers = 90
# the number of empty cars
cars_not_driven = cars - drivers
# the number of used cars
cars_driven = drivers
# the total seats that needed
carpool_capacity = cars_driven * space_in_a_car
# the average seats needed in a car
average_passengers_per_car = passengers / cars_driven

print 'There are', cars, 'cars available.'
print 'There are only', drivers, 'drivers available.'
print 'There are will be', cars_not_driven, 'empty cars today.'
print 'We can transport', carpool_capacity, 'people today.'
print 'We have', passengers, 'to carpool today.'
print 'We need to put about', average_passengers_per_car, 'in each car.'