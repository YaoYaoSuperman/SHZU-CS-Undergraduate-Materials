#!/usr/bin/env python3
#蒙特卡罗模拟三门问题
import random

pick_first_n,pick_scond_n = 0, 0 #初始化选择次数

times = eval(input("请输入你想要模拟的次数："))
for i in range(times): #int 要加 range() 函数
	car = random.randint(0, 2) #随机生成车在哪门后面
	choice = random.randint(0, 2) #选择
	if car == choice: #初始选择是对的
		pick_first_n += 1
	else:  
		pick_scond_n += 1 #主持人打开了一扇门，换门正确的情况
fWin = pick_first_n / times
sWin = pick_scond_n / times
print("坚持初选，胜率为：{:.2f}%".format(fWin*100))
print("改变选择，胜率为：{:.2f}%".format(sWin*100))
