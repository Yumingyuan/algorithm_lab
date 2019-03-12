def merge(need_sort_list):
	after_sort=[]
	print('Before sort:',need_sort_list)
	length=len(need_sort_list)
	if length%2==0:
		mid=int(length/2)
	elif length%2==1:
		mid=int(length/2)+1
	index1=0
	index2=mid
	for i in range(0,length):
		if index1>mid-1:
			after_sort.append(need_sort_list[index2])
			index2=index2+1
		elif index2>length-1:
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
	print('After sort:',after_sort)	
if __name__=='__main__':
	list_unsort=[2,10,13,18,19,1,3,5,7,9]
	list_unsort1=[1,3,5,7,9,2,10,13,18,19]
	list_unsort2=[1,3,5,7,9,2,6,10,13,18]
	list_unsort3=[1,7,8,10,3,4,5,6]
	merge(list_unsort)
	merge(list_unsort1)
	merge(list_unsort2)
	merge(list_unsort3)
