#!/usr/bin/env python3
#习题5.1 
def tian(n):
	for i in range(n):
		if i % 5 == 0:
			print("+--------------------+-------------------+")
		else:
			print("|                    |         			 |")
	print("+--------------------+-------------------+")
tian(24)
