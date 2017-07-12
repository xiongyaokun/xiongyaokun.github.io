#! /usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2017/7/7 9:43
# @Author  : xiongyaokun
# @Site    : 
# @File    : lexicon.py
# @Software: PyCharm

class Lexicon(object):

    def scan(self, sentence, standard_words, description):
        self.sentence = sentence
        self.words = sentence.split(' ')
        word_result = []
        for word in self.words:
            # 小错误要谨记啊! 不能再for循环内初始化变量啊
            # word_result = []
            try:
                word = int(word)
                word_result.append((description, '%s' % str(word)))
            except ValueError:
                if word in standard_words:
                    word = (description, '%s' % word)
                    word_result.append(word)

        return word_result