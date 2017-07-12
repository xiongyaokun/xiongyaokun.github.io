#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 16:49
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice47_tests.py
# @Software: PyCharm

from nose.tools import *
import NAME


def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"

