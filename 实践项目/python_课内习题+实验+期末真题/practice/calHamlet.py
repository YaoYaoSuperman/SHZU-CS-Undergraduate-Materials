#!/usr/bin/env python3
#calHamlet
def getText(): #归一化
	#读入文件～
	txt = open("hamlet.txt", "r").read() #果然放到同一个文件夹下面～
	txt = txt.lower() #every letters reform into lower
	for ch in '!"#$%&*+,-./:;<=>?@[\]^_‘{|}~':
		txt = txt.replace(ch, " ")
	return txt

hamletTxt = getText()
words = hamletTxt.split() #以空格为分割
counts = {} #词频统计 -> dictionary(字典 -> 键值对)
for word in words:
	counts[word] = counts.get(word, 0) + 1 #词频统计
items = list(counts.items())# 转化为列表类型 （key ？ or values ？）
items.sort(key = lambda x:x[1], reverse = True) #decline sorted
for i in range(10): #打印前十 高频
	word, count = items[i]	
	print("{0:<10}{1:>5}".format(word, count))
