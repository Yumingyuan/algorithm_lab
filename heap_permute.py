# -*- coding: utf-8 -*-
def heap_permute(data_set,n):
	if n==1:
		print(data_set[1:5])#切片
	else:
		for i in range(1,n):
			heap_permute(data_set,n-1)
			if n%2==1:
				data_set[1],data_set[n]=data_set[n],data_set[1]
			else:
				data_set[i],data_set[n]=data_set[n],data_set[i]
				#heap_permute(data_set,n-1)
if __name__=='__main__':
	data=[0,1,2,3]
	heap_permute(data,3)
