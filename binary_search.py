def binary_algorithm(search_data,low,high,data):
	result=0
	while low<=high and result==0:
		mid=int((low+high)/2)
		if search_data[mid]==data:
			result=mid
		elif  data<search_data[mid]:
			high=mid-1
		else:
			low=mid+1
	return result
if __name__=='__main__':
	search_data=[2,3,5,7,8,10,11,13,16,18]
	#print(
	print("location",binary_algorithm(search_data,0,len(search_data)-1,7))
