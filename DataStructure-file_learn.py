#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'

fhand = open('word_book.txt', 'a')
while(True):
    word = input('単詞を入りて　ください：')
    if word == 'end':
        break

    fhand.write((word + '\t'))
    pronounce = input('発声を入りて　ください： ')
    fhand.write((pronounce + '\t'))
    meaning = input('詞义を入りて　ください：')
    fhand.write((meaning + '\n'))

fhand.close()
hand = open('word_book.txt', 'r')
print(hand.read())
hand.close()



