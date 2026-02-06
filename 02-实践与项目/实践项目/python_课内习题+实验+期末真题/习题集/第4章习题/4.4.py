#!/usr/bin/env python3
import random 
random.seed(100) #随机种子 产生一个预设数字（后期不会改变）
tmp = random.randint(0, 100)#随机生成 0 - 10之间的整数
guess = eval(input("请输入您要猜的数字:"))
cnt = 0
while( guess != tmp):
	if guess < tmp:
		print("pity,your answer is smaller!")
		guess = eval(input("请再次输入您要猜的数字 :"))
	else:
		print("pity,your answer is bigger!")
		guess = eval(input("请再次输入您要猜的数字:"))
	cnt += 1
print("预测{:.0f}次，你猜中了！".format(cnt))

