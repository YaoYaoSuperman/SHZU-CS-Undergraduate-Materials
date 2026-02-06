#!/usr/bin/env python3
#求最大公约数
#辗转相除法 -> 利用模运算 -> 最大公约数 -> 最大公倍数
n, m = map(int, input("请输入两个整数：").split()) #接收多个数字的方法
tmp1, tmp2 = n, m
t = n % m
while(t): #余数为0 （可以整除的时候）
	n = m
	m = t
	t = n % m
cM = (tmp1 * tmp2 ) /  m
print("最大公约数是：{:.0f}, 最大公倍数是:{:.0f}".format(m, cM))
