# -*- coding: utf-8 -*-
#全排列问题
def Swap(perm_list,swap1,swap2):
	perm_list[swap2],perm_list[swap1]=perm_list[swap1],perm_list[swap2]
def Perm(perm_list,begin,end):
	if begin==end:
		print(perm_list)
	else:
		for i in range(begin,end):#对于每一个元素，进行交换并进行递归的perm调用
			Swap(perm_list,begin,i)#交换i与begin
			Perm(perm_list,begin+1,end)#继续交换后面的
			Swap(perm_list,i,begin)#恢复本轮交换的i与begin
if __name__=="__main__":
	num=int(input("input the num of permutation:"))
	list_perm=[i+1 for i in range(num)]
	Perm(list_perm,0,len(list_perm))
