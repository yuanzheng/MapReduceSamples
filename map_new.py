import sys
import time

for line in sys.stdin:
    ss = line.strip().split(' ')
    #time.sleep(100000)
    for word in ss:
        print '\t'.join([word.strip(), '1'])


# test: head -2 The_Man_of_Property.txt | python map_new.py
