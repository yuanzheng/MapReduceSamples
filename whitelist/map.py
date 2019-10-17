#!/usr/bin/python

import sys

def read_file(f):
    word_set = set()
    file_in = open(f, 'r')

    for line in file_in:
        word_set.add(line.strip())

    return word_set



def mapper_func(wordList):
    word_set = read_file(wordList)

    for line in sys.stdin:
        ss = line.strip().split(' ')
        
        for each in ss:
            word = each.strip()
            if word != "" and (word in word_set):
                print('\t'.join([word, '1']))



if __name__=="__main__":

    print ("hello world")
    ''' It allows to invoke method from command line explicitly!  '''
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None

    if len(sys.argv) > 1:
        args = sys.argv[2:]
    print(args)
    func(*args)
