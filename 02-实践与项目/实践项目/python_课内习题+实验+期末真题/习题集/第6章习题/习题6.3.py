#!/usr/bin/env python3
'''6.3 重复元素判定续。利用集合的无重复性改编程序练习题6.2的程序，获得个更快更简洁的版本。'''

def repetitionJudge(ls):
	set1 = set(ls)
	if len(set1) != len(ls):  #转化为集合后， 若元素有删减，说明有重复元素，return True
		return True
	return False

def main():
	ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
	print(repetitionJudge(ls))
main()
