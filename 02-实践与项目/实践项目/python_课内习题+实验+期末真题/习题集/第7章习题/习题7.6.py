#!/usr/bin/env python3
'''7.6修改程序练习题7.5的程序，使其能够对单词添加多重释义，
不同释义用逗号分开。'''
dict = {}
file = None
digits = '0123456789' 
path = 'dict1.txt'


def readWords():
	global file 
	file = open('xxx.txt', 'r', encoding = 'GBK')
	#存储为字符串，那样就就包括逗号
	string = file.read()
	
	
def searchMode():
	print('*' * 50)
	print('*' * 50)
	while True:
		word = input("(按数字键退出)想查的单词：")
		if word in digits:
			print('*' * 50)
			print('*' * 50)
			return
		print('------------------------------')
		try:
			print(dict[word])
		except KeyError:
			print("没有该单词！")
		print('------------------------------')
		
		
def editMode():
	print('*' * 50)
	print('*' * 50)
	while True:
		word = input("(按数字键退出)请输入你想添加或修改的单词：")
		if word in digits:
			print('*' * 50)
			print('*' * 50)
			return
		print('------------------------------')
		description = input("请输入您的解释：\n")
		try:
			dict[word] += ',%s'%description #含义理解！！
		except KeyError:
			dict[word] = '%s'%description
		print('------------添加完成------------')
		
def interface():
	readWords()
	def switch(option):
		funcdic = {
			1:lambda: searchMode(),
			2:lambda: editMode(),
			3:lambda: exit()
		}
		return funcdic[option]()
	while True:
		print('-----------欢迎使用英汉词典----------')
		print('1.查询单词\n2.添加单词\n3.退出\n')
		option = int(input('请输入您的选择:'))
		switch(option)
		
interface()
