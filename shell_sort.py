# -*- coding: utf-8 -*-
import random
range_upper=20
length=10
list_unsort=random.sample(range(range_upper),length)#生成随机数据集合
print('Before sort:',list_unsort)

gap=1
while gap<int(length/3):
	gap=gap*3+1#计算一个合适的gap值

while gap>=1:
	print("current gap:",gap)
	for i in range(int(gap),int(length)):
		j=i
		temp=list_unsort[j]#获取当前比较位置j的元素下标值
		print("current compare num:",temp)
		while j>=gap and list_unsort[j]<list_unsort[j-gap]:#把当前j与j-gap进行比较
			list_unsort[j]=list_unsort[j-gap]
			list_unsort[j-gap]=temp
			j=j-gap
			print("medium unsort list:",list_unsort)
	gap=int(gap/3)
	print("gap",gap)
print('After sort:',list_unsort)
	
			
