#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'

import string
import sys


while(True):
    fname = input('please enter the file name:')
    if fname == 'end':
        break
    else:
        try:
            fhand = open(fname, encoding='utf')
        except:
            print('the file is not exited!')
        mappe_1 = dict.fromkeys(i for i in range(sys.maxunicode) if chr(i) in string.punctuation)
        mappe_2 = dict.fromkeys(i for i in range(sys.maxunicode) if chr(i) in string.digits)
        mappe_3 = dict.fromkeys(i for i in range(sys.maxunicode) if chr(i) in string.whitespace)
        text = fhand.read()
        text = text.translate(mappe_1)
        text = text.translate(mappe_2)
        text = text.translate(mappe_3)
        text = text.lower()
        word = list(text)
        words = {}
        for i in word:
            if i in words:
                words[i] += 1
            else:
                words[i] = 0
        freq = []
        for k, v in words.items():
            freq.append((v, k))
        freq.sort(reverse=True)
        freq_1 = []
        for i in freq:
            freq_1.append((i[1], i[0]))
        print('The Top 10 of the file {0} is:\n '.format(fname) + str(freq_1[:10]))
        answer = input('where store the result to text file:(y or n):')
        answer = answer.lower()
        if answer == 'n':
            continue
        else:
            fhand_2 = open('freq.txt', 'a')
            fhand_2.write('the result of {0} frequency is:\n'.format(fname)
                          + str(freq_1[:10]) + '\n\n')
            fhand_2.close()





