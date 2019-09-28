import sys

word_dict = {}

with open('/Users/master/projects/BaDou/data/The_Man_of_Property.txt', 'r') as fd:
    for line in fd:
        ss = line.strip().split(' ')
        for w in ss:
            if w.strip() not in word_dict:
                word_dict[w.strip()] = 1
            else:
                word_dict[w.strip()] += 1

'''
for k,v in word_dict.items():
    print (k, v)
    
print (len(word_dict))
'''

word_list = [(k,int(v)) for k, v in word_dict.items()]
# sort by int(v), therefore, x[1]
word_list = sorted(word_list, key=lambda x:x[1], reverse=True)

for each in word_list:
    # print each
    print ('\t'.join([each[0], str(each[1])]))
