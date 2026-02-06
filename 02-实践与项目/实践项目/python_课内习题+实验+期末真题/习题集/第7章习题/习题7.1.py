#!/usr/bin/env python3
'''7.1 Python源文件改写。
编写一个程序，读取一个Python源程序文件，将文件中所有除保留字外的小写字母换成大写字母，
生成后的文件要能够被Python解释器正确执行。'''
import keyword

stopwords = '\t\n\r:()'
functionwords = '.('
word = []
output = ''
lastAvailable = ['from', 'import']
last = False

def readFile(path): #读取文件,返回为字符串类型
	file =  open(path, 'r', encoding = 'utf-8')
	string = file.read()
	return string[1:]

def parse(string): #分析读取的文本
	#全局变量
	global word
	global output
	global last
	for i in string:
		if i in stopwords:
			wd = ''.join(word) #word 赋值给 wd (中间什么都不加)
			res = isKeyWord(wd)
			if res == False: #标记是否是 导包 的关键字
				if i not in functionwords and last == False:
					wd = wd.upper()
			if wd in lastAvailable:
				last = True
			else:
				last = False
			output += wd
			output += i
			word = [] #重新初始化
		else:
			word.append(i)
			
def isKeyWord(stirng):
	if string in keyword.kwlist:
		return True
	return False

def outPutFile():
	file = open('/Users/luyao/Desktop/课内/python实验/习题集/第七章习题/ans_7.1.txt', 'w', encoding = 'utf-8')
	file.write(output)
			
string = readFile('/Users/luyao/Desktop/课内/python实验/习题集/第七章习题/test7_1.txt')
parse(string)
outPutFile()