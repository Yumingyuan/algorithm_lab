# -*- coding: utf-8 -*-
#全排列问题
def Swap(perm_list,swap1,swap2):
	perm_list[swap2],perm_list[swap1]=perm_list[swap1],perm_list[swap2]
	#print("swap",perm_list)
def Perm(perm_list,begin,end):
	if begin==end:
		print(perm_list)
	else:
		for i in range(begin,end):
			Swap(perm_list,begin,i)
			Perm(perm_list,begin+1,end)
			Swap(perm_list,i,begin)
if __name__=="__main__":
	num=int(input("input the num of permutation:"))
	list_perm=[i+1 for i in range(num)]
	Perm(list_perm,0,len(list_perm))
