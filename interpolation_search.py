# -*- coding: utf-8 -*-
import random
range_upper=30
length=20
def interpolation_search(datalist,key):
	low=0
	high=len(datalist)-1
	while low<=high:
		mid=int(low+(key-datalist[low])*(high-low)/(datalist[high]-datalist[low]))#通过公式计算最优mid值
		if mid<low or mid>high:#越界则忽略
			break
		if key<datalist[mid]:#当key小于mid索引到的值，则缩小区间向值更小的区域找
			high=mid-1
		elif key>datalist[mid]:#当key大于mid索引到的值，则缩小区间向值更大的区域找
			low=mid+1
		else:#相等情况则返回mid
			return mid
	return -1
if __name__=="__main__":
	test_list=random.sample(range(range_upper),length)#生成测试数据
	test_list.sort()#对数据进行排序
	print("test list:",test_list)#排序后结果
	print("result of 12:",interpolation_search(test_list,12))#搜索12的位置
	
