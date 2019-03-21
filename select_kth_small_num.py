# -*- coding: utf-8 -*-
import random
range_upper=100
length=43#默认数据集生成长度为45
def insert_sort(search_data,low,high):
	for i in range(low+1,high+1):
		j=i
		temp_num=search_data[j]#取出需要放在合适位置的数据
		while j>low and search_data[j-1]>temp_num:#向数组的首部逐个进行比较
			search_data[j]=search_data[j-1]#如果符合要求，则将更大的书向后挪1个位置
			j=j-1#继续向数组低位比较
		search_data[j]=temp_num#将比较数据放到合适他在的位置，这时已经在位了
def select(search_data,low,high,k):
	p=high-low+1#p的值将会是待select子数组元素个数
	small_list=[]
	equal_list=[]
	big_list=[]
	if p<44:#当数组规模小于等于44个时，直接进行排序然后返回相关位置的元素内容即可
		insert_sort(search_data,low,high)#调用插入排序
		return search_data[k-1]#返回相关位置元素
	else:
		q=int(p/5)
		middle_list=[]
		print("divide in to ",q,"groups")
		for i in range(0,q):
			insert_sort(search_data,low+i*5,low+i*5+4)#+4原因与insertsort的实现有关
			#print("After sort",search_data[low+i*5:low+i*5+5])
			middle_list.append(search_data[low+i*5+2])
		print("middle_list",middle_list)
		middle_list.sort()
		#print("sorted list",middle_list)
		mm=select(middle_list,0,q-1,int((q-1)/2+1))#获取中位数集合的中位数
		#print("middle middle:",mm)
		for i in range(low,high):
			if search_data[i]<mm:
				small_list.append(search_data[i])#比中位数集合的中位数小的数
			elif search_data[i]==mm:
				equal_list.append(search_data[i])#与中位数集合的中位数相等的数
			else:
				big_list.append(search_data[i])#比中位数集合的中位数大的数
		if len(small_list)>=k:
			return select(small_list,0,len(small_list)-1,k)
		if  len(small_list)+len(equal_list)>=k:
			return mm
		return select(big_list,0,len(big_list)-1,k-len(small_list)-len(equal_list))
		print(len(small_list))
		print(len(equal_list))
		print(len(big_list))
if __name__=="__main__":
	k=22
	test_list1=random.sample(range(range_upper),length)#生成list1
	print("before select list1：",test_list1)
	print("通过select方法选择的第k大数:",select(test_list1,0,len(test_list1)-1,k))
	test_list1.sort()#将数据列表直接调用系统排序进行，可以通过数数来判断位置
	print("验证结果是否正确:",test_list1)
	length=45#修改生成随机数据集长度为46
	test_list2=random.sample(range(range_upper),length)#生成list2
	print("before select list2：",test_list2)
	print("通过select方法选择的第k大数:",select(test_list2,0,len(test_list2)-1,k))
	test_list2.sort()#将数据列表直接调用系统排序进行，可以通过数数来判断位置
	print("验证结果是否正确:",test_list2)
	length=46
	test_list3=random.sample(range(range_upper),length)#生成list3
	print("before select list3",test_list3)
	#print("select result1:",select(test_list1,0,len(test_list1)-1,23))
	print("通过select方法选择的第k大数:",select(test_list3,0,len(test_list3)-1,k))
	test_list3.sort()#将数据列表直接调用系统排序进行，可以通过数数来判断位置
	print("验证结果是否正确:",test_list3)
