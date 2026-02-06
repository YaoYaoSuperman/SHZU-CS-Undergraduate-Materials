#!/usr/bin/env python3
'''7.2图像文件压缩。
使用PL库对图片进行等比例压缩，无论压缩前文件大小如何，
压缩后文件小于10KB。 '''
from PIL import Image
import os
import math

def getSize(path): #获取要压缩图片的大小
	return os.stat(path).st_size

def compress(path): #将图片变小（同时会损失清晰度），实验项目要求压缩
	size = getSize(path)
	ratio = math.sqrt(10 * 1024 / size)
	im = Image.open(path)
	height = im.height;
	width = im.width;
	m_height = int(ratio * height)
	m_width = int(ratio * width)
	ph = im.resize((m_width, m_height))
	ph.save("test_compress.jpg")
	
compress('/Users/luyao/Desktop/课内/python实验/习题集/第七章习题/学生证.jpg')