#!/usr/bin/env python3
#
#tf = open("hamlet.txt", "rt") #read txt (文本形式)
#for l in tf.readlines(100):
#	print(l)
#tf.close()
#import turtle as t
#t.title('自动轨迹绘制')
#t.setup(800, 600, 0, 0)
#t.pencolor("red")
#t.pensize(5)
##read data 
#datals = []
#f = open("data.txt")
#for line in f: #每行信息的读取（实现自动化）
#	line = line.replace("\n", "")
#	if line != '': #要加上条件非空判断 （eval函数）
#		datals.append(list(map(eval, line.split(","))))
#f.close()
##auto draw
#for i in range(len(datals)):
#	t.pencolor(datals[i][3], datals[i][4], datals[i][5])
#	t.fd(datals[i][0])
#	if datals[i][1]:
#		t.right(datals[i][2])
#	else:
#		t.left(datals[i][2])
#import wordcloud
##c = wordcloud.WordCloud()
##c.generate("wordcloud by Python")
##c.to_file("pywordcloud.png")
#import jieba 
#txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，他按照特定规则组织计算机指令，使得计算机能够自动进行各种运算处理"
#w = wordcloud.WordCloud( width = 1000, font_path = "Arial Unicode.ttf", height = 700)
#
#w.generate(" ".join(jieba.lcut(txt)))
#w.to_file("nihao.jpg")