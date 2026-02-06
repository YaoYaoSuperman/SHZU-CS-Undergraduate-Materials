#!/usr/bin/env python3
'''6.4 文本字符分析。
编写程序接收字符串，按字符出现频率的降序打印字母。
分别尝试录入(txt.read)一些中英文文章片段，比较不同语言之间字符频率的差别。'''
import jieba #process chinese

#英文统计(数据分析～)
#example:Being a winner is never an accident; winning comes about by design ,determination and positive action
def englishAnalysize():
	str = input("请输入一串字符:")
	str = str.lower() #全部转化为小写字母
	for ch in '!"#$%&*+,-./:;<=>?@[\]^_‘{|}~ ': #special character transform into NULL ~ 
		str = str.replace(ch, "")
#print(str, type(str))
	counts = {}  #初始化空字典（类比数组， key 相当于 index）
	
	for i in str:
		counts[i] = counts.get(i, 0) + 1; #key i 对应的 value （无值则利用预设值） + 1 赋值给 key i so that counts frequency 
	items = list(counts.items())  #转化为列表， 每一个元素是一个 tuple(元组)
	items.sort(key = lambda x: x[1], reverse = True) #以值作为排序关键字， 降序排序
#print NO.1 - 10
	for i in range(10): #遍历处理过的列表 并输 即可
		word , count = items[i]
		print("{0:<} : {1:<} 次".format(word, count))

#中文统计 -> jieba 库
#example : 生活不会向你许诺什么，尤其不会向你许诺成功。他只会给你挣扎、痛苦和煎熬的过程。所以要给自己一个梦想，之后朝着那个方向前进。
def chineseAnalysize():
	str = input("请输入一串字符:")
	str = jieba.lcut(str) #jieba.lcut 精准划分 （巧妙利用～）
#print(str, type(str))
	counts = {}  #初始化空字典（类比数组， key 相当于 index）
	
	for i in str:
		counts[i] = counts.get(i, 0) + 1; #key i 对应的 value （无值则利用预设值） + 1 赋值给 key i so that counts frequency 
		if i in ['、', '，', '。', ' ']:
			del counts[i] 
	items = list(counts.items())  #转化为列表， 每一个元素是一个 tuple
	items.sort(key = lambda x: x[1], reverse = True) #以值作为排序关键字， 降序排序
#print NO.1 - 10
	for i in range(10): #遍历处理过的列表 并输 即可
		word , count = items[i]
		print("{0:<10}:{1:<5} 次".format(word, count))
#chineseAnalysize()
englishAnalysize()