#!/usr/bin/env python3
#对《三国演义》生成词云
import wordcloud
import jieba

#以只读模式打开文本文件
f = open("threekingdoms.txt","r", encoding = "utf-8")
txt = f.read()
f.close() 
#别忘了关闭文件， 有始有终
w = wordcloud.WordCloud(font_path = "Arial Unicode.ttf",  width = 1000, height = 700, background_color = "white",
	max_words = 100)
#wordcloud & jieba 有机结合
w.generate(" ".join(jieba.lcut(txt)))
w.to_file("三国演义词云.png")