def merge(need_sort_list,low,mid,high):
	after_sort=[]
	index1=low
	index2=mid+1
	for k in range(low,high+1):
		if index1>mid:
			after_sort.append(need_sort_list[index2])
			index2=index2+1
		elif index2>high:
			after_sort.append(need_sort_list[index1])
			index1=index1+1
		elif need_sort_list[index1]<need_sort_list[index2]:
			after_sort.append(need_sort_list[index1])
			index1=index1+1
		elif need_sort_list[index1]>need_sort_list[index2]:
			after_sort.append(need_sort_list[index2])
			index2=index2+1
		else:
			pass
	print("After merge:",after_sort)
def sort(need_sort_list,low,high):
	if high<=low:
		return 
	mid=int(low+int((high-low)/2))
	print('current sort:',need_sort_list[low:high+1],"low mid and high:",low,mid,high)
	sort(need_sort_list,low,mid)
	sort(need_sort_list,mid+1,high)
	merge(need_sort_list,low,mid,high)
if __name__=='__main__':
	list_unsort=[2,10,13,18,19,1,3,5,7,9]
	print("before_sort:",list_unsort)
	sort(list_unsort,0,len(list_unsort)-1)
