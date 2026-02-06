#!/usr/bin/env python3
'''7.4CSV解析。
改编实例14，使得对CSV的转换能够识别并保留数据内部的逗号。'''
import json
f = open("xxx.csv", 'r')
lister = []
for line in f:
	line = line.replace("[", "")
	line = line.replace("]", "")
	line = line.replace(" ", "")
	line = line.replace("\n", "")
	for i in line.split("'"): #分割
		if i != ',':
			lister.append(i)
f2 = open('xxx.json', 'w')
for r in range(1, len(lister)):
	lister[r] = dict(zip(lister[0], lister[r]))
json.dump(lister[1:], f2, sort_keys = True, indent = 4, ensure_ascii = False)
print("转换完成")
f2.close()
f.close()