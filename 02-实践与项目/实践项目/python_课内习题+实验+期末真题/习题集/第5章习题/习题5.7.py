#!/usr/bin/env python3
#Hanoi问题 -> abstract
cnt = 0 #记录移动的次数 
def Hanoi(n, src, dst, mid): #src -> source 源柱子; destination -> 目的柱子
	global cnt #global variance,值最终会传递给main函数
	if n == 1: #只剩最大的盘子时，递归出口
		print("只剩一个", n)
		print("{}:{}->{}".format(1, src, dst))
		cnt += 1
	else:
		print("进入递归",n)
		Hanoi(n-1, src, mid, dst) #将n-1个圆盘 搬到中间
		print("回溯")
		print("{}:{}->{}".format(n, src, dst)) #第n最大的圆盘搬到C上（问题分解为这样了）
		cnt += 1 #计数
		Hanoi(n-1, mid, dst, src) #再将n-1个圆盘 移到C柱子上
Hanoi(3, 'A', 'C', 'B')
print("移动的次数为:",cnt)
