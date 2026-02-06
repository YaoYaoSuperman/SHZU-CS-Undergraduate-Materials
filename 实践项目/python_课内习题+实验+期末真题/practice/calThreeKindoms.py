#!/usr/bin/env python3
#
import jieba

#读入文件～
txt = open("threekingdoms.txt", "r", encoding = "utf - 8").read() #果然放到同一个文件夹下面～
excludes = {"将军", "却说", "荆州", "二人", "不可", "不能", "如此"}
#jieba 调用
words = jieba.lcut(txt)#list cut -> acquisite divide
counts = {}

for word in words: #traverse
	if len(word) == 1:
		continue
	elif word == "诸葛亮" or word == "孔明曰":
		rword = "孔明"
	elif word == "关公" or word == "云长":
		rword = "关羽"
	elif word == "玄德" or word == "玄德曰":
		rword = "刘备"
	elif word == "孟德" or word == "丞相":
		rword = "曹操"
	else:
		rword = word
	counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
	del counts[word] #delete key & value
	
items = list(counts.items())# 转化为列表类型 （key ？ or values ？ cell?）
#print(items) 
items.sort(key = lambda x:x[1], reverse = True) #decline sorted
for i in range(10): #打印前十 高频
	word, count = items[i] #return type is : cell ~
	print("{0:<10}{1:>5}".format(word, count))
