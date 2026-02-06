#!/usr/bin/env python3
from random import*
#体育竞技分 -> 蒙特卡罗模拟～
#高聚态  低耦合 （提高代码复用度）
# 乒乓球比赛规则：
# 在一局比赛中，先得11分的一方为胜方

def printIntro():
	print("这个程序模拟两个选手A和B的乒乓球比赛")
	print("程序运行需要A和B的能力值（以0到1之间的小数表示）")
	
def getInputs():
	a1 = eval(input("请输入选手A的能力值："))
	a2 = eval(input("请输入选手B的能力值："))
	n  = eval(input("模拟比赛的场次："))
	return a1, a2, n #返回元素类型
	
def sinNGames(n, proA, proB): #继续向下划分
	winsA, winsB = 0, 0
	for i in range(1, n + 1):
		scoreA, scoreB = sinOneGames(proA, proB)
		if scoreA > scoreB:
			winsA += 1
		else:
			winsB += 1
	return winsA, winsB
		
def sinOneGames(proA, proB):
	scoreA, scoreB = 0, 0
	serving = "A"
	while not gameOver(scoreA, scoreB):
		if serving == "A":
			if random() < proA: #在选手A的能力区间， 模拟选手A的胜利～
				scoreA += 1
			else: 
				serving = "B"
		else:
			if random() < proB:
				scoreB += 1
			else:
				serving = "A"
	return scoreA, scoreB

def gameOver(scoreA, scoreB):
	if scoreA == 11 or scoreB == 11:
		return 1 #比赛结束
	return 0
	
def printSummary(n, winsA, winsB):
	print("共模拟{}场比赛".format(n))
	#注意格式化方法～
	print("A赢了:{}次，占比:{:0.1%}".format(winsA, winsA / n))
	print("B赢了:{}次，占比:{:0.1%}".format(winsB, winsB / n))

printIntro()
probA, probB, n= getInputs()
winsA, winsB = sinNGames(n, probA, probB)
printSummary(n, winsA, winsB)