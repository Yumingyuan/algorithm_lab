# -*- coding: utf-8 -*-
def merge(data,low,mid,high):
	global count
	i=low
	k=low
	j=mid+1
	#count=0
	temp=[0 for i in range(len(data))]
	while i<=mid and j<=high:
		if data[i]>data[j]:
			#i及i右侧到mid的元素都比A[j]大，由于在A[j]左侧所以逆序
			count+=(mid-i+1)
			temp[k]=data[j]
			k+=1
			j+=1
		else:#没有逆序的情况
			temp[k]=data[i]
			i+=1
			k+=1
	#当i越过mid或j越过high时则没越过的那一边元素顺序正确且没有逆序
	while i<=mid:
		temp[k]=data[i]
		k+=1
		i+=1
	while j<=high:
		temp[k]=data[j]
		k+=1
		j+=1
	for i in range(low,high+1):#将调整顺序的数据放入data中用于后续计算
		data[i]=temp[i]
	print("After merge",data,"count:",count)
def sort(need_sort_list,low,high):
	if high<=low:
		return 
	mid=int((low+high)/2)
	print('current sort data:',need_sort_list[low:high+1],"low mid and high:",low,mid,high)
	sort(need_sort_list,low,mid)
	sort(need_sort_list,mid+1,high)
	merge(need_sort_list,low,mid,high)
if __name__=='__main__':
	global count
	count=0
	list_unsort=[1,7,2,9,6,4,5,3]
	#print("before_sort:",list_unsort)
	sort(list_unsort,0,len(list_unsort)-1)
	print("count num",count)
