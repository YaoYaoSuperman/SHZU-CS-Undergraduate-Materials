#!/usr/bin/env python3
#习题5.2 

def isOdd(n):
	if n % 2 == 0:
		return True
	else:
		return False
num = eval(input("Please input an integer:"))
print(isOdd(num))
