#!/usr/bin/env python3
from  datetime  import*

bd = datetime(2002, 6, 4, 12, 30 ) #
print(bd)
print('%s-%s-%s'%(bd.year, bd.month, bd.day)) # %号形式
print('{0:%Y}-{0:%m}-{0:%d} {0:%a}'.format(bd)) # %a返回周几
print('{0:%b}.{0:%d}.{0:%Y}'.format(bd)) # %b返回 月份
print('{0:%d}{1:} {0:%b} {0:%Y}'.format(bd, ['st', 'nd', 'rd', 'th'][bd.day%10-1 if bd.day%10 <= 3 else 3]))
