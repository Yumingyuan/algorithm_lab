# -*- coding: utf-8 -*-
def insert_sort(search_data,low,high):
	for i in range(low+1,high+1):
		j=i
		temp_num=search_data[j]#to insert's num compare from i-1 to low
		while j>low and search_data[j-1]>temp_num:
			search_data[j]=search_data[j-1]#move [j-1] to [j]
			j=j-1
		search_data[j]=temp_num#make the temp_num the right place
def QuickSort(search_data,low,high):
	if high>low:
		k=Partitions(search_data,low,high)
		if (k-1-low)<=9 and (high-k-1)<=9:#当基准元素左侧右侧的规模小于等于9时，进行插入排序
			print("low,high,k,left and rigth both need insert:",low,high,k)
			insert_sort(search_data,low,k-1)
			insert_sort(search_data,k+1,high)
		elif (k-1-low)<=9 and (high-k-1)>9:#当基准元素左侧规模小于等于9且右侧的规模大于9时，左侧进行插入排序，右侧快排
			print("low,high,k,left need insert right need quick:",low,high,k)
			insert_sort(search_data,low,k-1)
			QuickSort(search_data,k+1,high)
		elif (k-1-low)>9 and  (high-k-1)<=9:#当基准元素左侧规模大于9且右侧的规模小于等于9时，左侧进行快排，右侧插入排序
			print("low,high,k,left need quick and right need insert:",low,high,k)
			QuickSort(search_data,low,k-1)
			insert_sort(search_data,k+1,high)
		elif (k-1-low)>9 and (high-k-1)>9:#当基准元素左侧规模大于9且右侧的规模小于等于9时，左侧进行快排，右侧插入排序
			print("low,high,k,left and right need quick::",low,high,k)
			QuickSort(search_data,low,k-1)
			QuickSort(search_data,k+1,high)
		else:
			pass
def Partitions(search_data,low,high):
	left=low
	right=high
	reference=search_data[low]#最低位元素作为基准元素，通过后续while循环为其寻找合适的位置
	while left<right:
		while search_data[left]<=reference:#基准元素大于left获得的元素值，说明符合小于基准元素的值在基准元素左侧，向后查
			left=left+1
		while search_data[right]>reference:#基准元素小于right获得的元素值，说明符合小于基准元素的值在基准元素左侧，向后查
			right=right-1
		if left<right:#交换不符合要求的left和right元素位置
			search_data[left],search_data[right]=search_data[right],search_data[left]
	search_data[low]=search_data[right]#当跳出while left<right循环时，right的值肯定小于基准元素
	search_data[right]=reference#将基准元素放到合适位置
	return right#返回基准元素位置信息
if __name__=="__main__":
	unsort_list=[0,4,5,3,2,7,9,1,11,8,12,134,76,33,22,57]
	print("before sort:",unsort_list)
	QuickSort(unsort_list,0,len(unsort_list)-1)
	print("After sort:",unsort_list)
