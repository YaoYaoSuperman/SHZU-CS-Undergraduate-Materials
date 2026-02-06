#!/usr/bin/env python3
import wordcloud
import jieba
from scipy.misc import imread
mask = imread("fiveStar.jpeg")
#以只读模式打开文本文件
f = open("新时代中国特色社会主义.txt","r", encoding = "utf-8")
txt = f.read()
f.close() 
#别忘了关闭文件， 有始有终
w = wordcloud.WordCloud(font_path = "Arial Unicode.ttf",mask = mask,  width = 1000, height = 700, background_color = "white",
	max_words = 15)
#wordcloud & jieba 有机结合
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("hello.png")