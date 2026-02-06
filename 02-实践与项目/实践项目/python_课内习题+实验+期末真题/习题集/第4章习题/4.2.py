#!/usr/bin/env python3
s = input("请输入一行字符：") #eval 评估
kong, alpha, chinese, num, other = 0, 0, 0, 0, 0

for i in s: #for循环遍历用户输入字符
	if i == " ":
		kong += 1
	elif  '0' <= i <= '9':
		num += 1
	elif u'\u4e00' <= i <= u'\u9fa5': #unicode中文区间
		chinese += 1
	elif True == i.isalpha():
		alpha += 1
	else:
		other += 1
print("空格，数字，中文，英文字符，其他字符分别有{:.0f},{:.0f},{:.0f},{:.0f},{:.0f}个".format(kong, num, chinese,alpha, other))
		
		
