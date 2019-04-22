# -*- coding: utf-8 -*-
def QuickSort(search_data,low,high):
	if high>low:
		k=Partitions(search_data,low,high)#获取关键元素 被放置在数组中的什么位置
		QuickSort(search_data,low,k-1)
		QuickSort(search_data,k+1,high)
def Partitions(search_data,low,high):
	left=low
	right=high
	reference=search_data[low]
	while left<right:
		while search_data[left]<=reference:
			left=left+1
		while search_data[right]>reference:
			right=right-1
		if left<right:
			search_data[left],search_data[right]=search_data[right],search_data[left]
	search_data[low]=search_data[right]
	search_data[right]=reference
	return right
if __name__=="__main__":
	unsort_list=[0,4,5,3,2,7,9,1,11,8,12]
	print("before sort:",unsort_list)
	QuickSort(unsort_list,0,len(unsort_list)-1)
	print("After sort:",unsort_list)
