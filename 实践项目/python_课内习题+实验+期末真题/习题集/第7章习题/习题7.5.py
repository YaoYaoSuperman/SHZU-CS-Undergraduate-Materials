#!/usr/bin/env python3
'''7.5制作英文学习词典。
编写程序制作英文学习词典，词典有3个基本功能： 添加、查询和退出。
程序读取源文件路径下的txt格式词典文件，若没有就创建个。
词典文件存储方式为“英文单词中文单词”，每行仅有一对中英释义。
程序会根据用户的选择进入相应的功能模块，并显示相应的操作提示。
当添加的单词已存在时，显示“该单词已添加到字典库”；当查询的单词不存在时，显示“字典库中未找到这个单词”。
用户输入其他选项时，提示“输入有误”。'''

dict = {}
digits = '0123456789' 
path = 'dict1.txt'

def readFile(path, arg):
	file = open(path, arg, encoding = 'GBK')
	return file

def readWords():
	file = readFile(path, 'r')
	while True:
		line = file.readline() #按行读取
		if not line:
			break
		word = line.split('  ', 2)
		dict[word[0]] = word[1][:-1]
	file.close()

def writeFile(word, dsp):
	file = readFile(path, 'a')
	file.write('{} {}\n'.format(word, dsp))
	file.close()
	
def modifyFile(word, dsp):
	file = readFile(path, 'r')
	line = file.readlines()
	flen = len(line) - 1
	for i in range(flen):
		if word in line[i]:
			file.close()
			line[i] = '{} {}\n'.format(word, dsp)
			file = readFile(path, 'w')
			file.writelines(line)
			break
	file.close()
	
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
		try:
			print('该单词已存在于词库，当前解释是：{}'.format(dict[word]))
		except:
			print('您添加的是一个新单词')
		print('------------------------------')
		description = input("请输入您的解释：\n")
		try:
			dict[word] += ',%s'%description #含义理解！！
			modifyFile(word, dict[word])
		except KeyError:
			dict[word] = '%s'%description
			writeFile(word, dict[word])
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
		
		