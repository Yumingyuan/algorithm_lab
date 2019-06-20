# -*- coding: utf-8 -*-
count=0
def merge(data,low,mid,high):
	i=low
	k=low
	j=mid+1
	count=0
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
	print("After merge",temp)
def sort(need_sort_list,low,high):
	if high<=low:
		return 
	mid=int(low+int((high-low)/2))
	print('current sort data:',need_sort_list[low:high+1],"low mid and high:",low,mid,high)
	sort(need_sort_list,low,mid)
	sort(need_sort_list,mid+1,high)
	merge(need_sort_list,low,mid,high)
if __name__=='__main__':
	list_unsort=[2,10,13,18,19,1,3,5,7,9]
	print("before_sort:",list_unsort)
	sort(list_unsort,0,len(list_unsort)-1)
