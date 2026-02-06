#!/usr/bin/env python3
'''6.5 生日悖论分析。
生日悖论指如果一个房间里有23人或以上，那么至少有两个人生日相同的概率大于50%。
编写程序，输出在不同随机样本数量下，23个人中至少两个人生日相同的概率。'''
from random import*

def birthSame(ls): #利用集合的确定性判断重复元素
	set1 = set(ls)
#	print(set1)
	if len(set1) != len(ls): #集合 -> 判断重复元素 !!(相同元素的问题)
 		return 1 #return numbers of people that birthday is same
	return 0 #不相同

#蒙特卡罗仿真模拟～
n = eval(input("请输入随机次数:"))
poss = 0
for i in range(n): #随机模拟次数
	people = {} #initialization null dictionary
	for i in range(0, 24): #23 个人生日 随机模拟
		mon = randint(1, 12) 
		day = randint(1, 30)
		birth = (mon, day) #元组类型
		people[i] = birth
	ls = list(people.values())
	if birthSame(ls) == 1:
		poss += 1  #poss 记录最终符合条件的次数
print("在随机{:}次下，23个人中至少两个人生日相同的概率:{:.2f}".format(n, poss*100/n))

