#!/usr/bin/env python3 （python3编译？？底层原理！！）
from time import*
scale = 50
print("执行开始".center(scale // 2, '-')) #center 第一个参数返回为 全部长度，满足对称python自动调节
t1 = perf_counter()
for i in range(scale):
	a = '*' * i
	b = '-' * (scale - (i+1)) #从0开始哟！！
	c = (i+1)*2
	dur = perf_counter() - t1
	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end = " ") #定义元素类型！！
	sleep(0.01) #让时间 “睡一会儿” -> 显示刷新率！！
print("\n" + "执行结束".center(scale // 2, '-'))