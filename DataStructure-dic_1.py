#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'
while(True):
    fname = input('please enter the file name:')
    hisg = {}
    if(fname == 'end'):
        break
    else:
        try:
            fhand = open(fname)
            for line in fhand:
                if(line.startswith('From')):
                    line = line.split('@')
                    dona = line[1]
                    dona = dona.split()[0]
                    hisg[dona] = hisg.get(dona, 0) + 1
        except:
            print('sorry, the file is not exitted, please check it!')
        finally:
            commit = []
            for k, v in hisg.items():
                commit.append((v, k))
            commit.sort(reverse=True)
            print(commit[0][1], commit[0][0])






