#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/7 10:07
# @Author  : xiongyaokun
# @Site    : 
# @File    : lexicon_tests.py
# @Software: PyCharm

from nose.tools import *
import lexicon

DIRECTION = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
VERBS = ['go', 'stop', 'kill', 'eat']
STOP = ['the', 'in', 'of', 'from', 'at', 'it']
NOUNS = ['door', 'bear', 'princess', 'cabinet']
# NUMBERS = [i for i in range(10)]
NUMBERS = "0987654321234567890"


lexicon1 = lexicon.Lexicon()

def test_directions():
    assert_equal(lexicon1.scan("north", DIRECTION, 'direction'), [('direction', 'north')])
    result = lexicon1.scan("north south east", DIRECTION, 'direction')
    assert_equal(result, [('direction', 'north'),
                          ('direction', 'south'),
                          ('direction', 'east')])

def test_verbs():
    assert_equal(lexicon1.scan("go", VERBS, 'verb'), [('verb', 'go')])
    result = lexicon1.scan("stop kill eat", VERBS, 'verb')
    assert_equal(result, [('verb', 'stop'),
                          ('verb', 'kill'),
                          ('verb', 'eat')])

def test_stop():
    assert_equal(lexicon1.scan('the', STOP, 'stop'), [('stop', 'the')])
    result = lexicon1.scan("in of from at", STOP, 'stop')
    assert_equal(result, [('stop', 'in'),
                          ('stop', 'of'),
                          ('stop', 'from'),
                          ('stop', 'at')])

def test_nouns():
    assert_equal(lexicon1.scan('door', NOUNS, 'noun'), [('noun', 'door')])
    result = lexicon1.scan("bear princess cabinet", NOUNS, 'noun')
    assert_equal(result, [('noun', 'bear'),
                          ('noun', 'princess'),
                          ('noun','cabinet')])

def test_number():
    assert_equal(lexicon1.scan('1234', NUMBERS, 'number'), [('number', '1234')])
    result = lexicon1.scan("3 91234", NUMBERS, 'number')
    assert_equal(result, [('number', '3'),
                          ('number', '91234')])
