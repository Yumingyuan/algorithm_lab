# -*- coding: utf-8 -*-
def heap_permute(data_set,n):
	print("heap's:",n,data_set)
	if n==1:
		print(data_set[1:])#切片
	else:
		for i in range(1,n+1):#从1到n
			heap_permute(data_set,n-1)
			if n%2==1:
				data_set[1],data_set[n]=data_set[n],data_set[1]#交换元素1与n的位置
			else:
				data_set[i],data_set[n]=data_set[n],data_set[i]#交换元素i与n的位置
				#heap_permute(data_set,n-1)
if __name__=='__main__':
	input_num=int(input("num need permute>"))
	data=[i for i in range(input_num+1)]
	heap_permute(data,input_num)
