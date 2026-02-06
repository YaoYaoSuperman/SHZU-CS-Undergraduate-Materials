#!/usr/bin/env python3
#描述性统计(高内聚， 低耦合)
def getNum():
	nums = [] #define a list
	
	iNumStr = input("请输入a digit(回车退出):")
	while iNumStr != "": #eval() -> 字符串解码
	#只能一个一个接收
		nums.append(eval(iNumStr)) #list 后面添加元素
		iNumStr = input("请输入数字(enter to end)")
	return nums

def mean(nums):
	n = len(nums)
	sum = 0
	
	for i in nums:
		sum += i
		
	return sum // n

def variance(nums, mean): #utilize mean to calculate the varaiance
	n = len(nums)
	sum_2 = 0
	
	for i in nums: #cycle 实现累加
		sum_2 += (i - mean) ** 2
		
	return pow((sum_2 // n - 1), 0.5)

def midDigit(nums):
	sorted(nums) #increasing sorted
	n = len(nums)
	
	if n % 2 == 0:
		x1 = (nums[(n - 1) // 2] + nums[((n - 1) // 2) + 1] ) // 2
	else:
		x1 = nums[(n - 1) // 2]
		
	return x1

ls = getNum()
print(ls)
mean1 = mean(ls)
print(mean(ls))
print(variance(ls, mean1))
print(midDigit(ls))