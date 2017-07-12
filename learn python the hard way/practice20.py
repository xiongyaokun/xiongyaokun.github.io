#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/5 0:30
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice20.py
# @Software: PyCharm
from sys import argv

script, input_file = argv

# 打印文件内的所有内容
def print_all(f):
    print f.read()
    # f.close()

def rewind(f):
    f.seek(0)

# 打印单行内容
def print_a_line(line_count, f):
    print line_count, f.readline()


current_file = open(input_file)


print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
# current_line = current_line + 1
current_line += 1
print_a_line(current_line, current_file)

current_file.close()