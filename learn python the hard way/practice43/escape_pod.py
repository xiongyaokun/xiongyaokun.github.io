#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/6 14:28
# @Author  : xiongyaokun
# @Site    : 
# @File    : escape_pod.py
# @Software: PyCharm
from random import randint


def escape_pod():
    print "You rush through the ship desperately trying to make it to the escape pod before the whole ship explodes." \
          "It seems like hardly any Gothons are on the ship, so you run is clear of interference. You get to the chamber" \
          "with the escape pods, and" \
          "now need to pick one to take. Some of them could be damaged but you don't have time to look. There's 5 pods, which" \
          "one do you take?"
    good_pod = randint(1,5)
    guess = raw_input("[pod #]")


    if int(guess) != good_pod:
        print "You jump into pod %s and hit the eject button." % guess
        print "The pod escapes out into the void of space, them implodes as the hull ruptures, crushing your body into " \
              "jam jelly."
        return 'death'
    else:
        print "You jump into pod %s and hit the eject button." % guess
        print "The pod easily slides out into space heading to the planet below. As it flies to the planet, you look back" \
              "and see your ship implode then explode like a bright star, taking out the Gothon ship at the same time." \
              "You won!"
        exit(0)
