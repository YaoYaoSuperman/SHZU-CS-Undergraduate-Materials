#!/usr/bin/env python3
'''6.2 
重复元素判定。
编写一个函数，接受列表作为参数，如果一个元素在列表中出现了不止一次，则返回True,但不要改变原来列表的值。
同时编写调用这个函数和测试结果的程序。'''

def repetitionJudge(ls):
	for i in ls:
		if ls.count(i) == 2: #出现重复元素（函数功能模块），借力打力
			return True
	return False

def main():
	ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
	print(repetitionJudge(ls))
main()
