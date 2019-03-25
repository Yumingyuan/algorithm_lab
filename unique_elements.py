# -*- coding: utf-8 -*-
import random
range_upper=30
length=20
def unique_element_cmp(data_list):
	for i in range(len(data_list)-1):#从0扫描到n-2,依次检测相邻的元素是否一致(由于已经排序好，)
		#保证一旦有相同的元素，则排序后数据一定有相邻元素一定是一致的
		if data_list[i]==data_list[i+1]:
			return False
	return True
if __name__=="__main__":
	test_list1=random.sample(range(range_upper),length)#生成测试数据(保证不重复)
	test_list1.sort()#对数据进行排序
	test_list2=[1,3,7,5,2,3,5,8,11,25]
	test_list2.sort()
	print("After sort:",test_list1)
	print("Unique or not:",unique_element_cmp(test_list1))
	print("After sort:",test_list2)
	print("Unique or not:",unique_element_cmp(test_list2))
