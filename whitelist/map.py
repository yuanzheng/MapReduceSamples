#!/usr/bin/python

import sys

def test(wordList):
    print (wordList)


if __name__=="__main__":

    print ("hello world")
    ''' It allows to invoke method from command line explicitly!  '''
    module = sys.modules[__name__]
    func = getattr(module, sys.argv[1])
    args = None

    if len(sys.argv) > 1:
        args = sys.argv[2:]

    func(*args)
