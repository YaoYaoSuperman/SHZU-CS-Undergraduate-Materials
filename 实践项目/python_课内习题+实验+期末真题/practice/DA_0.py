#!/usr/bin/env python3
#a = 1 
#
#def hellworld():
#	print("hello,world!")
#	
#def facotr(n):
#	if(n == 0):
#		return 1
##	print(n)
#	return n * facotr(n-1)
#	
#while a < 10: #a < 10 为循环终止条件（语言都是相通的，更重要的是内功！！）
#	a += 2
#	if a >= 7:
#		print(a)
#		print(">=7！")
#	else:  
#		pass #pass 和 continue 功效一样？？ 底层逻辑？？	fa
#print(facotr(5))

#异常捕获 （try exception） 检查程序的错误 （发射卫星， 火箭，出错损失太惨重了！）
#try:
#	print(1/0) #发生异常时， 程序终止，直接跳转到except, else不执行
#except Exception as e:
#	print(3)
#	print(e)
#else:
#	print(4)
#	print("no exception") #没有例外 -> 无漏洞
##programing block
#	
#try:
#	print(1/1) #没有异常，直接进入else(不提示出错信息)
#	#主体程序块（自己编写的代码， 编程思维！）
#except Exception as e:
#	print(1)
#	print(e)
#else:
#	print(2)
#	print("no exception")
#
#try:
#	print(1/1)
#except:
#	print("exception happen!")
#else:
#	print("try success")
#finally: #不论是否成功都会进入！(必经之路)
#	pass

#python经典数据结构
#1.python 原生数据结构: 元组 Tuple() ,列表 List[],集合 Set{},字典（对集合的扩充，键值对） Dictionary{A:B}
#不用导入包
#tup1 = ('Google', 'Runoob', 1997, 2000)
#tup2 = (1,)
#tup3 = ()
#print(tup1, tup2, tup3)

#2.NumPy 包中的数据结构:数组 Ndarray(带多种操作)，矩阵 Matrix(多种线性代数计算)
import numpy as np #巧妙利用好别人已经造好的轮子！！

#3.Pandas 包中的数据结构: 序列 Series(索引+1列数据)，数据框 DataFrame(索引+多列数据表)
import pandas as pd
dic1 = {'name':['Tom', 'Lily', 'Cindy', 'Petter'],
	    'no':['001', '002', '003', '004'], 
		'age':[16, 16, 15, 16], 
		'gender':['f', 'm', 'm', 'f']}
df1 = pd.DataFrame(dic1)
print("该数据结构的类型是",type(df1))
print('\n',dic1)