#dayup = 1.0
#n = 1.0
#dayfactor = 0.01
#for i in range(365):
#	if i % 7 in [6, 0]: #计算机模拟休息日/工作日！！
#		dayup = dayup*(1-dayfactor)
#	else:
#		dayup = dayup*(1+dayfactor)
#		#抽象 + 自动化！！
#		#dayup = pow(1 + datfactor, 365)
#		#daydown = pow(1 - datfactor, 365)
#for i in range(365):
#	n = n * (1 + dayfactor)
#print(n)
#	
#print("工作日的努力参数是：{:.2f}".format(dayup))

#def dayUp(df): #返回值为 一个数字
#	dayup = 1
#	for i in range(365):
#		if i % 7 in [0, 1, 2]:
#			pass #连续三天能力值不变
#		elif i % 7 in [3, 4, 5, 6]:
#			dayup = dayup * (1 + df)
#	return dayup; 
#dayfactor = 0.01
#while dayUp(dayfactor) < 37.78 : #不断试错，逼近正确答案
#	dayfactor += 0.001
#print("365天后能力值是：{:.2f}".format(dayUp(dayfactor))) #precision -> 精度
#print("工作日的努力参数是: {:.3f}".format(dayfactor))

	
#抽象 + 自动化
#def dayUp(df):
#	dayup = 1
#	for i in range(365):
#		if i % 7 in [6, 0]: #计算机模拟休息日/工作日！！
#			dayup = dayup*(1-df)
#		else:
#			dayup = dayup*(1+df)
#	return dayup;
#dayfactor = 0.01
#while dayUp(dayfactor) < 37.78:
#	dayfactor += 0.001
#print("工作日努力程度的参数是：{:.3f}".format(dayfactor))

#n = 0.01
#off = [10, 15] #隔10天休息 or 15天
#for k in off:
#	capacity = 1 #初始能力值
#	j = 0 #记录休息的次数
#	for i in range(365): #模拟365天 （蒙特卡罗模拟）
#		if i%k != 0:  #当不是休息日
#			if (i - (k + 1)*j) % 7 not in [1, 2, 0]:
#				print((i - (k + 1)*j)  )
#				capacity *= (1+n)
#			else: #连续三天能力值不增加
#				continue
#		else: #i % k == 0
#			j += 1
#			print(i)
#			continue
#	print("{:-^20.2f}\n{:.0f}".format(capacity,j))		


#def stay(x):#模型函数
#	dayup =1.00#初始⽔平值
#	day =0#10天休息⼀天
#	cycle =0#周期
#	for i in range(365):
#		if day==x or cycle ==7:#10天休息⼀天，重新开始计算天数,7天为⼀周期
#			day =0 #休息10天后， 一切重新开始
#			cycle =0
#		else: #当不休息的时候 （if嵌套，条件由外及内，层层深入）
#			if day%7 in [3,4,5,6]:#后四天能⼒增长
#				dayup = dayup *(1+0.01)
#				day = day +1
#			else:
#				day = day +1
#				cycle = cycle +1
#				print(day, cycle)
#	print("每{}天休息⼀天365天后能⼒值：{:.2f}".format(x,dayup))
#stay(10)#调⽤模型函数
#stay(15)

#def growUp(x): #定义成长函数 -> 建模
#	capacity = 1.00
#	 #factor -> 系数
#	day = 0  #休息后 进行更新（间断周期从0开始计算）
#	cycle = 0 #周期 -> 更新
#	for i in range(365):
#		if day == x or cycle == 7: #休息or周期已到，重置
#			day = 0
#			cycle = 0
#		else: #周期不进行更新的时候（最外层条件）
#			if day % 7 in [3, 4, 5, 6]:
#				capacity *= (1 + 0.01)
#				day += 1
##				cycle += 1
#			else: #努力却效果不是很高的阶段
#				day += 1
#				cycle += 1 
#	print("每{:.0f}天一休息，365天后的能力值：{:.2f}".format(x,capacity))		
#growUp(10)
#growUp(15)
	
#dayup = 1 #初始能力值
#dayfactor = 0.01 #增长系数
#period = [4, 5, 6, 0] #能力增长的日子
#decrease = 0 
#for j in range(1, 366): #1 -> 355天模拟
#	temp = j -decrease
#	tom = temp % 7 #tom模拟一周中的up ｜ down
#	if j % 15 == 0: #休息日
#		decrease += j - (tom - 1)
#		tom = 1 #初始化
#	if tom in period:
#		dayup *= (1 + dayfactor)
#print('rest every fifteen days,the result is %.2f'%( dayup))
#		
#WeekNamePrintV1.py
#weekStr = "一二三四五六日"
#weekId = eval(input("请输入星期数字（1-7）："))
#
#print("星期" + weekStr[weekId -1]) #观察到了 输入 和 字符串 之间的关系，一定要有雄厚且扎实的基础

#tmpStr = input("输入一个字符串：")
#print("{:.0f}".format(len(tmpStr)))

#for i in range(12):
#	print(chr(9800 + i), end = " ")

#处理字符串string的常用功能（方法，method）
#print("AbCdEfGh".lower()) #全部转化为小写字母
#print("asdafnsd".upper()) #化为大写
#print("A,B,C".split("，")) #字符串分割
#print("an apple a day".count('a')) #注意：子串在str中出现的次数
#print("python".replace("thon", "yao")) #替换子串
#print("python".center(20, "=")) #居于中心，（宽度，填充字符）
#print("= python=".strip((" =np"))) #跳过用户指定字符
#print(",".join("12345")) #在每个字符中间加‘,’ -> 字符串分割

#字符串类型的格式化 .format
#print("{1}:计算机{0}的CPU占用率为{2}%".format("2018-10-10", "C", 10)) #槽(从0开始计数哦～)
##第一组：填充(用什么填充)，对齐（左，中，右），宽度（数字）【字符串输出格式】
#print("{:=^20}".format("PYTHON"))
#print("{:*>20}".format("PYTHON"))
#print("{:*<20}".format("PYTHON"))
#print("{:10}".format("BIT")) #默认左对齐，填充空格
##第二组： <.> <精度> <类型>
#print("{:,.2f}".format(12345.6789))
#print("{0:b}, {0:c}, {0:d}, {0:o}, {0:x}, {0:X}".format(425)) #不加0会报错！ （加0的底层原理？）
#print("{0:e}, {0:E}, {0:f}, {0:%}".format(3.14))

#import time 
#def wait():
#	time.sleep(3.3)
#	
#print(time.time())
#print(time.ctime())
#t = time.gmtime()
##时间格式化
#print(time.strftime("%Y-%m-%d %H:%M:%S", t))
#timeStr = "2018-01-26 12:55:20"
#start = time.perf_counter()
#print(time.strptime(timeStr, "%Y-%m-%d %H:%M:%S"))
#end = time.perf_counter() #perfect_counter ~~(完美计算时间)
#wait()
#result = end - start
#
##时间计时
#print(result)

#文本进度条
#import time
#scale = 50 #文本条的宽度
#print("执行开始".center(scale//2, "-")) #居中对齐格式～～ center函数
#start = time.perf_counter()
#for i in range(scale + 1): #循环结构
#	a = '*' * i 		# ‘*’->由少至多 ｜  字符串 * i -> 字符串复制了i次 for循环 up（基础知识！！）
#	b = '.' * (scale - i)	#‘. ’ -> 由多至少
#	c = (i / scale) * 100 #百分比计算
#	dur = time.perf_counter() - start
#	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end = " ") #三个槽 制造 动画效果～～
#	time.sleep(0.1) #产生动画效果
#	#加 \r 配合 end = “ ” 涮洗效果 -> 动画
#print("\n"+ "执行结束".center(scale//2, '-'))

#刷新的关键字为/r
#for i in range(101):
#	print("\r{:3}%".format(i), end = " ")
#	time.sleep(0.01)
#
#import time 
#scale = 50 #规模～
#print("执行开始".center(scale//2, "-"))
#start = time.perf_counter()
#for i in range(scale ):
#	a = '*'*i
#	b = '.'* (scale - (i +1) )
#	c = (i + 1 ) * 2
#	dur = time.perf_counter() - start
#	print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c, a, b, dur), end = " ")
#	time.sleep(0.01)
#print("\n"+ "执行成功".center(scale//2, "-"))

#测试用例 12321 12345
#for i in range(11):
#	if i in [0, 5, 10]:
#		print("+-----+----+")
#	else:
#		print("|     |    |")
#	
from time import sleep
print("Starting",end = '') #加end -> 不自动换行
for i in range(10):
	print("..", end = '')
	sleep(0.1)
print("Done!")