# -*- coding: utf-8 -*-
def divide(data,left,right):
	if (right-left)<=1:#只有两个或一个元素的情况
		if data[left]<data[right]:
			return left
		else:
			return right
	else:
		mid=int((left+right)/2)
		left_min=divide(data,left,mid)
		right_min=divide(data,mid+1,right)
		if data[left_min]<data[right_min]:
			return left_min
		else:
			return right_min
if __name__=="__main__":
	test_data=[0,1,3,6,-2,5,7]
	print(divide(test_data,0,len(test_data)-1))
