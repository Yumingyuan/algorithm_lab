def insert_sort(search_data,low,high):
	for i in range(low+1,high+1):
		j=i
		temp_num=search_data[j]#to insert's num compare from i-1 to 0
		while j>low and search_data[j-1]>temp_num:
			search_data[j]=search_data[j-1]
			j=j-1
		search_data[j]=temp_num
def QuickSort(search_data,low,high):
	if high>low:
		k=Partitions(search_data,low,high)
		if (k-1-low)<=9 and (high-k-1)<=9:
			print("low,high,k,left and rigth both need insert:",low,high,k)
			insert_sort(search_data,low,k-1)
			insert_sort(search_data,k+1,high)
		elif (k-1-low)<=9 and (high-k-1)>9:
			print("low,high,k,left need insert right need quick:",low,high,k)
			insert_sort(search_data,low,k-1)
			QuickSort(search_data,k+1,high)
		elif (k-1-low)>9 and  (high-k-1)<=9:
			print("low,high,k,left need quick and right need insert:",low,high,k)
			QuickSort(search_data,low,k-1)
			insert_sort(search_data,k+1,high)
		elif (k-1-low)>9 and (high-k-1)>9:
			print("low,high,k,left and right need quick::",low,high,k)
			QuickSort(search_data,low,k-1)
			QuickSort(search_data,k+1,high)
		else:
			pass
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
	unsort_list=[0,4,5,3,2,7,9,1,11,8,12,134,76,33,22,57]
	print("before sort:",unsort_list)
	QuickSort(unsort_list,0,len(unsort_list)-1)
	print("After sort:",unsort_list)
