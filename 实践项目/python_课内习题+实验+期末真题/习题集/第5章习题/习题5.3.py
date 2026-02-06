#!/usr/bin/env python3
#python中合法的数字有 十进制，浮点数， 十六进制整数，复数
#-------3 也为合法数字！ 
#注意降低强程序的敏感性
def isNum(num):
	np = '+-' #character
	numbers = ".0123456789" 
	numbersE = '.+-jJEe0123456789' #带科学计数法的digit
	x16 = "0123456789abcdefABCDEF" #16进制表示
	
	if num[0] in np: #当首字符是符号时
		try: #异常处理机制
			return isNUm(num[1:]) #递归调用，向下遍历 string
		except:
			return False #
	elif num[0] in numbers:
		if num[:2] == '0x': # is 0x
			for i in num[2:]: #traverse to check 
				if i not in x16:
					return False #inputed wrong string
			return True 
		else: 
			ele = 0
			point = 0
			last = ''
			numaftere = 0
			q = 0
			for i in num: #多条件判断！！
				q = q + 1
				if i not in numbersE:
					return False
				else:
					if point == 0 and i == '.':
						point = 1
						continue
					if point == 1 and (numaftere == 1 or ele == 0) and i in '+-':
						point = 0
						continue
					if ele == 0 and i in 'Ee': #初夏按了第一个E，一个浮点数中只能出现一个E
						ele = 1
						continue
					if ele == 1 and i in '0123456789':
						numaftere = 1
						continue
					if ele == 1 and numaftere == 1 and i in '+-':
						ele = 0
						numaftere =  0
						continue
					if last == '.' and i in '+-':
						return False
					elif(point == 1 or last in 'EeJj') and i == '.':
						return False
					elif i in 'Jj' and last in '+-':
						return False
					elif ele == 1 and i in "Ee.":
						return False
				lsat = i
			if last == '.' and i in '+-':
				return False
			elif(point == 1 or last in 'EeJj') and i == '.':
				return False
			elif i in 'Jj' and last in '+-.':
				return False
			elif ele == 1 and i in "Ee.":
				return False
			else:
				return True
	else: #after cycle ending ~
		return False	
print(isNum('hello'))
print(isNum('0x16'))
print(isNum('+++'))
print(isNum("0.100"))
print(isNum("999"))


