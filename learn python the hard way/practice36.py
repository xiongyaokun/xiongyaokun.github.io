#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/17 22:46
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice36.py
# @Software: PyCharm

# 'and' example
print "'and'example:"
print "False and 12 is:", False and 12

# 'del' example, 'del'只是删除引用，
if __name__ == "__main__":
    a = 1
    b = a
    c = b
    del b, c
    print "'del'example:"
    print a

# lists 中保存的是变量 lists[0],lists[1..., 而不是真实的数据 0，1，2，3，4，5
if __name__ == "__main__":
    lists = [0, 1, 2, 3, 4, 5]
    a = lists[0]
    del lists[0]
    print "'del'example:"
    print a

# 'assert' example, assert是声明其断言值必须为真的语法，如果发生异常就说明表达式为假
# assert  2 == 1, '2不等于1'  #会报异常
# assert 2 == 2              #不会报异常

# 'isinstance' example,
isinstance('Hello', str)


