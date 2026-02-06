#!/usr/bin/env python3
#6.6 《红楼梦》人物统计。编写程序统计《红楼梦》中前20位出场最多的人物。
# 类比三国演义 出场人物统计即可， 本质都是相通的～
import jieba.posseg as ps

#读入文件～
txt = open("红楼梦.txt", "r", encoding = "utf - 8").read() #果然放到同一个文件夹下面～
excludes = {"明白"}
#jieba 调用
words = ps.cut(txt) #list cut -> acquisite divide
counts = {}

#-------------------------core steps----------------------
for w in words: #traverse
	if len(w.word) == 1: #一个字 不是人命， 继续下一个元素的遍历
		continue
	if w.flag == 'nr': # is people's name
		counts[rword] = counts.get(rword, 0) + 1
for w in excludes:
	del counts[w] #delete key & value
#--------------------------------------------------------
	
items = list(counts.items())# 转化为列表类型 （key ？ or values ？ cell?） -> 全部转化为cell
#print(items) 
items.sort(key = lambda x:x[1], reverse = True) #decline sorted（对列表类型进行排序）
for i in range(20): #打印前二十 高频
	word, count = items[i] #return type is : cell ~ （二元赋值）
	print("{0:<10}{1:>5}".format(word, count))