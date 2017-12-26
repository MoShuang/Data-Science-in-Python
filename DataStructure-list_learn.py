#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'

fname = input('please enter the filename:')
try:
    fhand = open(fname)
    words = []
    for line in fhand:
        word_temp = line.split()
        for word in word_temp:
            if (word not in words):
                words.append(word)
    words.sort()
    print(words)
except:
    print('The file is not exited!')
finally:
    print('Thank you for using.'
          '')

