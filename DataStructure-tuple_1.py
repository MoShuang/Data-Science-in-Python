#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'
fname = input('please enter the file name:')
try:
    hours = {}
    fhand = open(fname)
    for line in fhand:
        if((line.startswith('From')) &(not line.startswith('From:'))):
            hour = line.split(':')[0]
            hour = hour.split()[-1]
            hours[hour] = hours.get(hour, 0) + 1
except:
    print('sorry, the file is not exited!')
finally:
    hour_inod = []
    for k, v in hours.items():
        hour_inod.append((k, v))
    hour_inod.sort()
    print(hour_inod)



