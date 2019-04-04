# -*- coding: utf-8 -*-
import random
import time
def min_max_method1(search_data):#穷举搜索
	length=len(search_data)
	temp_max=search_data[1]
	temp_min=search_data[1]
	for i in range(2,length):#从第二个元素进行对比
		if search_data[i]>temp_max:
			temp_max=search_data[i]
		if search_data[i]<temp_min:
			temp_min=search_data[i]
	return temp_max,temp_min
def min_max_method2(search_data,low,high):
	#the situation of only two number
	if high-low<=1:
		if search_data[low]<search_data[high]:
			return (search_data[high],search_data[low])
		else:
			return (search_data[low],search_data[high])
	#the situation of more number than 2
	mid_num=int((low+high)/2)
	x1,y1=min_max_method2(search_data,low,mid_num)
	x2,y2=min_max_method2(search_data,mid_num+1,high)
	if x1<x2:
		x=x2
	else:
		x=x1
	if y1<y2:
		y=y1
	else:
		y=y2
	return x,y
if __name__=="__main__":
	range_upper=200
	length=15
	list_search=random.sample(range(range_upper),length)
	print('Before search:',list_search)
	starttime=time.time()
	print(min_max_method1(list_search))
	endtime=time.time()
	print("function1 time consuming:",(endtime-starttime),"s")
	starttime=time.time()
	print(min_max_method2(list_search,0,len(list_search)-1))
	endtime=time.time()
	print("function2 time consuming:",(endtime-starttime),"s")
