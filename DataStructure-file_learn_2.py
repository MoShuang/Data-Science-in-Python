#!/user/bin/env python
# -*- coding: utf-8 -*-
_author_ = 'MoShuang'


while(True):
    fname = input('文書の名前を入りて　ください：')
    try:
        fhand = open(fname)
        count = 0
        for line in fname:
            count +=1
        print('これは{0}行ですよ。'.format(count))
        continue
    except:
        if fname == 'na na boo boo':
            print('NA NA BOO BOO TO YOU, 貴方は阿呆ですか・' )
        else:
            print('すみませんがここに　この文書がありません。')
    finally:
        if fname == 'end':
            print('いらしやいます')
            break
exit()
