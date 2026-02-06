#!/usr/bin/env python3
#习题5.4
def multi(*args): #实现函数多参数输入（不限个数）
	sum = 1
	try:
		for i in args:
			sum *= i
		return sum
	except:
		print("参数有误！")
print(multi(3, 5, 4, 4, 1.3 ))
print(multi("love you three thounds\n", 6))
	