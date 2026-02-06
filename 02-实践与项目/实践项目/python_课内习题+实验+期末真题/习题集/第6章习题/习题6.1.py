#!/usr/bin/env python3
#6.1 随机密码生成。编写程序，在26个字母大小写和9个数字组成的列表中随机生成0个8位密码

import random as ram

ls = []
for i in range(65, 123): #ASCII码值相对应
	if chr(i) in [ '[', '\\', ']', '^', '_', '`']:
		continue
	ls.append(chr(i))
for i in range(0, 9):
	ls.append(i) #ls's element number is 61
	
#print(ls[0], ls[60])	
for i in range(0, 10):
	print("第{:}个随机密码: ".format( i + 1), end = "")
	for i in range(0, 8):
		index = ram.randint(0, 60) #in the interval : [0, 62] to generate random integer
		print(ls[index], end = "")
	print('\n')
	