#!/usr/bin/env python3
#9.4 
#自定义规律绘制。参考实例18, 绘制你感兴趣的一个数学或物理规律
import numpy as np 
import pylab as pl 
import matplotlib.font_manager as fm #设置字体格式
import matplotlib 
#设置x的范围， [0, 2pi] 间隔为0.001 -> 近似认为连续
t=np.arange(0.0,2.0*np.pi,0.001)
#以t为自变量画sin函数
s=np.sin(t)
#以t为自变量画cos函数
z=np.cos(t)
#在同一个坐标系之下画两个函数
pl.plot(t,s,label='正弦')  #（x, y, 标记[marker]）
pl.plot(t,z,label='余弦')
#指定系统自带的字体
font = fm.FontProperties(fname = '/Library/Fonts/Arial Unicode.ttf')
#打印x 轴的标签
pl.xlabel('x-变量',fontproperties = font,fontsize=10)
#打印y 轴的标签
pl.ylabel('y-正余弦的函数值',fontproperties= font,fontsize=10)
#打印标题（title）
pl.title('sin-cos函数图像',fontproperties= font,fontsize=18)
pl.show()