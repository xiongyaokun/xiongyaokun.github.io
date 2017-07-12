#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/6/17 18:50
# @Author  : xiongyaokun
# @Site    : 
# @File    : practice35.py
# @Software: PyCharm

from sys import exit

# when the game starts, if choose the 'right' door, you will enter the gold_room.
def gold_room():
    global how_much
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number!")

    if how_much >= 50:
        print "Nice, you are hot greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

# when the game starts, if you choose the 'left' door, you will enter this bear_room.
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of money."
    print "The fat beat is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

# a devil
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# tell you the end of this game, and the reason that you failed the game!
def dead(why):
    print why, "Good job!"
    exit(0)


# start this game, this is the game entrance
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()


