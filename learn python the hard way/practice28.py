#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/9 0:02
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice28.py
# @Software: PyCharm

print "True and True:", True and True
print "False and True:", False and True
print "1 ==1 and 2 ==2:", 1 == 1 and 2 == 2
print '"test" == "test":', "test" == "test"
print "1 == 1 or 2 != 1:", 1 == 1 or 2 != 1
print "True or 1 == 1:", True or 1 == 1
print "\"test\" == \"testing\":", "test" == "testing"
print "1 != 0 and 2 == 1:", 1 != 0 and 2 == 1
print "\test\" != \"testing\":", "test" != "testing"
print "'test' == 1:", "test" == 1
print "not (True and False):", not(True and False)
print "not(1 == 1 and 0 != 1):", not(1 == 1 and 0 != 1)
print "not(10 == 1 or 1000 == 1000):", not(10 ==1 or 1000 == 1000)
print "not(1 != 10 or 3 == 4):", not(1 != 10 or 3 == 4)
print "not(\"testing\" == \"testing\" and \"Zed\" == \"Cool Guy\"):", not('testing' == 'testing' and 'Zed' == 'Cool Guy')
print "1 == 1 and not(\"testing\" == 1 or 1 == 0):"
print 1 == 1 and not('testing' == 1 or 1 == 0)
print "\"Chunky\" == \"bacon\" and not (3 == 4 or 3 == 3):"
print 'Chunky' == 'bacon' and not (3 == 4 or 3 == 3)
print "3 == 3 and not (\"testing\" == \"testing\" or \"Python\" == \"Fun\"):"
print 3 == 3 and not ('testing' == 'testing' or 'Python' == 'Fun')
