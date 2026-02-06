#!/usr/bin/env python3
#life is short, you need python~
#函数 + 递归 实现 求 结成（递归）【分（二分）治～】
#n = 1
#def factor(n, m = 1): #可选参数～未获得参数，那么使用设定的默认值
##	global n #全局变量声明（函数调用会改变变量的值，类比指针）
#	if  n == 0:
#		return 1;
#	return n * factor(n-1);
#
##def BinaryFind(a[], low, high): #递归实现 二分查找？？
#
##谨慎使用lmabda定义匿名函数
#f = lambda x, y : x + y #lambda函数调用
#f1 = lambda : "lambda函数"
#
#print(f1())

#七段数码管的绘制
#高内聚， 低耦合
#无欲则刚，添坎卦 补 离卦（细细品味）
import turtle as t
import time as tm
def drawLine(draw): #画一条线（同样的性质）
	t.pendown() if draw else t.penup()
	t.fd(40)
	t.right(90)
	
def drawDigit(digit): #数字特点进行绘制
	drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
	drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
	drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
	drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
	t.left(90)
	drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
	drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
	drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
	t.left(180)
	t.penup()
	t.fd(20)
#	t.done()
	
def drawDate(date): #data,format is '%Y- %m= %d+'
	t.pencolor("red")
	for i in date: #judge every character
		if i == '-':
			t.write('年', font = ("Arial", 18, "normal"))
			t.pencolor("green")
			t.fd(40)
		elif i == '=':
			t.write('月', font = ("Arial", 18, "normal"))
			t.pencolor("blue")
			t.fd(40)
		elif i == '+':
			t.write('日', font = ("Arial", 18, "normal"))
		else:
			drawDigit(eval(i))
			
def main():
	t.speed(1000)
	t.setup(800, 350, 200, 200)
	t.penup()
	t.fd(-300)
	t.pensize(5)
	drawDate(tm.strftime('%Y-%m=%d+', tm.gmtime())) #上文函数调用
	print(tm.strftime('%Y-%m=%d+', tm.gmtime())) #2022-09=13+
	t.hideturtle()
	t.done()

def rvs(s): #递归实现字符串反转
	if s == "":
		return s;
	else:
		return rvs(s[1:]) + s[0]

def Fibnacci(n):
	if n == 1 or n == 2:
		return 1
	else:
		return Fibnacci(n-1) + Fibnacci(n-2)

#Hanoi问题 -> abstract
cnt = 0
def Hanoi(n, src, dst, mid): #src -> source 源柱子; destination -> 目的柱子
	global cnt #global variance
	if n == 1:
		print("{}:{}->{}".format(1, src, dst))
		cnt += 1
	else:
		Hanoi(n-1, src, mid, dst) #将n-1个圆盘 搬到中间
		print("{}:{}->{}".format(n, src, dst)) #第n最大的圆盘搬到C上
		cnt += 1 #计数
		Hanoi(n-1, mid, dst, src) #再将n-1个圆盘 移到C柱子上
#Hanoi(3, 'A', 'C', 'B')
#print(cnt)
		
def koch(size, n):
	
	if n == 0: #基例
		t.fd(size)
	else:	#链条
		for angle in [0, 60, -120, 60]:
			t.left(angle)
			koch(size/3, n-1)
def main():
	t.setup(600, 600)
	t.speed(9999999999999999999999999999999999999999999999999999999999999999999)
	t.penup()
	t.goto(-200, 100)
	t.pendown()
	t.pensize(2)
	level = 5
	koch(400, level) #第一次调用
	t.right(120)
	koch(400, level) #第二次调用
	t.right(120)
	koch(400, level) #第三次
	t.hideturtle()
main()
	