#!/usr/bin/env python3
import jieba
with open('沉默的羔羊.txt', 'r', encoding='utf-8') as f:
	#读取为txt文件
	txt = f.read()
	words = jieba.lcut(txt)
	counts = {}
	for word in words:
		if len(word) == 1:
			continue
		else:
			counts[word] = counts.get(word, 0) + 1;

ls = list(counts.items())
#以第二个元素为基准，由高到低进行排序
#注意重写的格式！
ls.sort(key = lambda x:x[1], reverse = True)

print(ls[0][0])