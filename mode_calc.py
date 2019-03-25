# -*- coding: utf-8 -*-
import random
range_upper=30
length=20
def mode_calc(sorted_data_list):
	length=1
	max_mode_frequency=0
	max_mode_num=0
	for i in range(len(sorted_data_list)):
		value=sorted_data_list[i]
		#不超过长度，且值一直相等，则频率长度length一直自增1
		while i+length<=(len(sorted_data_list)-1) and value==sorted_data_list[i+length]:
			length+=1
		if length>max_mode_frequency:#跳出后进行频率比较
			max_mode_frequency=length
			max_mode_num=value
		i=i+length#跳过length，不用再计算
	print("frequency:",length,"mode num:",max_mode_num)
if __name__=="__main__":
	test_list1=[0,1,3,5,1,7,1,4,8,9,2,1]
	test_list2=random.sample(range(range_upper),length)#生成测试数据(保证不重复)
	test_list1.sort()#排序了
	print("test list1:",test_list1)
	mode_calc(test_list1)#模式计算
	test_list2.sort()#排序
	print("test list2:",test_list2)
	mode_calc(test_list2)#由于元素不重复，所以只有list[0]的元素被认为频率最高，因为后面的元素频率都是1,没有超过if的条件
