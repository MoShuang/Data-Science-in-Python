#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'

string = 'Hello, this is just a test line.\nFrom moshuang1233@outlook.com ' \
'Sat\nFrom 981517367@qq.com Fri\nFrom yau.edu.com Fri\n'
string  = string.split('\n')
count = {}
for line in string:
    if(line.startswith('From')):
        line = line.split()
        wd = line[2]
        count[wd] = count.get(wd, 0) + 1
print(count)
