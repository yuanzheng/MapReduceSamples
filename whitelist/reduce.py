#!/usr/bin/env python

import sys


def reduce_func():
    cur_word = None
    sum = 0

    for line in sys.stdin:
        ss = line.strip().split('\t')

        if len(ss) != 2:
            continue

        word, cnt = ss

        if cur_word == None:
            cur_word = word

        if cur_word != word:
            print('\t'.join([cur_word, str(sum)]))
            cur_word = word
            sum = 0

        sum += int(cnt)

    print('\t'.join([cur_word, str(sum)]))





if __name__=="__main__":

    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])

    func()





