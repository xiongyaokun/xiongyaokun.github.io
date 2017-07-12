#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/7 9:43
# @Author  : xiongyaokun
# @Site    : 
# @File    : lexicon.py
# @Software: PyCharm


DIRECTION = ['direction', 'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
VERBS = ['verb', 'go', 'stop', 'kill', 'eat']
STOP = ['stop', 'the', 'in', 'of', 'from', 'at', 'it']
NOUNS = ['noun', 'door', 'bear', 'princess', 'cabinet']
# NUMBERS = [i for i in range(10)]
NUMBERS = "0987654321234567890"

# DESCRIPTION = [DIRECTION, VERBS, STOP, NOUNS]
descriptions = [DIRECTION, VERBS, STOP, NOUNS]
class Lexicon(object):

    def scan(self, sentence):
        self.sentence = sentence
        self.words = sentence.split(' ')
        word_result = []
        # print self.words
        for word in self.words:
            try:
                num = str(word)
                num = int(num)
                word_result.append(('number', '%s' % str(num)))
            except ValueError:
                for index, description in enumerate(descriptions):
                    if word in description:
                        # 小错误要谨记啊! 不能再for循环内初始化变量啊
                        # word_result = []
                        word1 = (description[0], '%s' % word)
                        word_result.append(word1)
                        # break 跳出当前循环
                        break
                    else:
                        if index == len(descriptions)-1:
                            word_result.append(('error', '%s' % word))
        return word_result