#!/usr/bin/env python3
'''7.3 中文字符画。
参考实例12，编写程序合理选取中文字符构造字符表，
生成中文字符画。'''
from PIL import Image

unicode_char = list('')

def get_char(r, g, b, alpha = 256): #获取字符
	if alpha == 0:
		return ' '
	gray = int(0.2126*r + 0.7152*g + 0.0722*b)
	unit = 256/len(ascii_char)
	return unicode_char[int(gray // unit)]

def main(filename):
	im = Image.open(filename)
	WIDTH, HEIGHT = 100, 60
	im = im.resize((WIDTH, HEIGHT))
	txt = ''
	for i in range(HEIGHT):
		for j in range(WIDTH):
			txt += get_char(*im.getpixel((j, i))
		txt += '\n'
	fo = open('pic_' + filename + 'txt', 'w')
	fo.write(txt)
	fo.close()
	
main('/Users/luyao/Desktop/课内/python实验/习题集/第七章习题/学生证.jpg')