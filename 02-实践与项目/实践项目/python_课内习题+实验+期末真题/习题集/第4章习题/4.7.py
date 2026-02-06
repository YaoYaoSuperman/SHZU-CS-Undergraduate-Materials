#!/usr/bin/env python3
str = input("请输入带有符号的温度值：")
if str[-1] in ['f', 'F']:
	try: #try - except 程序异常处理，增强健壮性～
		C = (eval(str[:-1]) - 32) / 1.8
		print("转换后的温度是：{:.2f}C".format(C))
	except:
		print("您输入的温度格式有误！")
elif str[-1] in ['c', 'C']:
	try:
		F = 1.8 * eval(str[:-1]) + 32
		print("转换后的温度是：{:.2f}F".format(F))
	except:
		print("您输入的温度格式有误！")
else:
	print("您输入的温度格式有误！")