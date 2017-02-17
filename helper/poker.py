#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

"""
    suit  - 牌面花色：
        ['h', 'hearts', 'd', 'diamonds', 's', 'spades', 'c', 'clubs']
        值对应红桃，方块，黑桃，梅花, 'h', 'd', 's', 'c' 是缩略写法
    point - 牌面点数：
        ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'O', 'JOKER']
"""
__joker__ = 'JOKER'
__points__ = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
__suits__ = ['h', 'd', 's', 'c']
__Pais__ = []

__pais__ = []
for suit in __suits__:
    for point in __points__:
        pai = '%s.%s' % (suit, point)
        __pais__.append(pai)
    __Pais__.append('%s.%s' % (suit, __joker__))
__Pais__.extend(__pais__ * 2)


def deal_card():
    random.shuffle(__Pais__)
    result = [[], [], [], []]

    for i in range(0, len(__Pais__)-8, len(result)):
        for j in range(len(result)):
            index = i+j
            result[j].append(__Pais__[index])

    result.append(__Pais__[-8:])
    return result


if __name__ == '__main__':
    result = deal_card()
    for res in result:
        print len(res)
        #print res
