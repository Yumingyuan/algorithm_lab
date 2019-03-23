# -*- coding: utf-8 -*-
import random
range_upper=20
length=10
list_unsort=random.sample(range(range_upper),length)#随机生成长度10,随机数范围20以内的数据集
print('Before sort:',list_unsort)#在排序之前进行输出

for i in range(1,length):#从第1个元素进行扫描比较，持续到数组最后
	j=i
	temp_num=list_unsort[j]#获取第i个元素
	while j>0 and list_unsort[j-1]>temp_num:#temp元素与i-1到0这些下标的元素比较，找到合适位置
		list_unsort[j]=list_unsort[j-1]#将位置后移动，为i腾出位置
		j=j-1#遍历
	list_unsort[j]=temp_num
print('After sort:',list_unsort)
	
