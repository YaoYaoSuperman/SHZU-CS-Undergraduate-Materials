#!/usr/bin/env python3
import random 
import types #type函数判断类型
random.seed(100) #随机种子 产生一个预设数字（后期不会改变）
tmp = random.randint(0, 100)#随机生成 0 - 10之间的整数
cnt = 0
while 1 :
	try:
		guess = eval(input("请输入您要猜的数字:")) 
		if type(guess) == type(1):
			cnt += 1
			if guess < tmp:
				print("pity,your answer is smaller!")
			elif guess > tmp:
				print("pity,your answer is bigger!")
			else:
				print("预测{:.0f}次，你猜中了！".format(cnt))
				break #预测成功，那么停止循环
	except: #try语句块 出现报错，那么执行except中的语句
		print("输入内容必须为整数！")
	

