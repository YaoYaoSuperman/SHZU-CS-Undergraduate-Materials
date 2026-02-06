#!/usr/bin/env python3
import math 

def isPrime(n):
	try: #exception 处理机制
		if type(n) == type(0.):
			raise TypeError
	except TypeError:
		print("类型错误！")
		return None
	if n == 1:
		return False
	for i in range(2, int (math.sqrt(n)) + 1): #range() 函数 !! 实现范围～
		if n % i == 0:
#			print(i)
			return False
	return True
print(isPrime(7))
print(isPrime(21))
print(isPrime(1))
print(isPrime(1.5))

