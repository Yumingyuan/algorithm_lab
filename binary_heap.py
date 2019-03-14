def left(search_data,i):
	set_length=len(search_data)
	if i==0 or 2*i>set_length-1:
		return
	else:
		return 2*i
def right(search_data,i):
	set_length=len(search_data)
	if i==0 or 2*i+1>set_length-1:
		return
	else:
		return 2*i+1
def parent(search_data,i):
	if i==1:
		print("Root Node!")
		result=search_data[i]
	elif i>len(search_data)-1:
		print("too huge")
		result=0
	elif i/2>=1:
		result=search_data[int(i/2)]
	return result
def height(search_data,i):
	count=0
	start=i
	while left(search_data,start) is not None:
		start=start*2
		count=count+1
	return count
def heapify(search_data,i):
	left_num=left(search_data,i)
	right_num=right(search_data,i)
	largest=0
	if left_num is None:
		return
	elif right_num is not None and left_num is not None:
		if left_num<len(search_data) and search_data[left_num]>search_data[i]:
			largest=left_num
		else:
			largest=i
		if left_num<len(search_data) and search_data[right_num]>search_data[largest]:
			largest=right_num
		if largest!=i:#need exchange
			temp=search_data[i]
			search_data[i]=search_data[largest]
			search_data[largest]=temp
			print("heapify:",i,search_data)
		heapify(search_data,largest)
	elif right_num is None and left_num is not None:
		if left_num<len(search_data) and search_data[left_num]>search_data[i]:
			largest=left_num
		else:
			largest=i
		if largest!=i:#need exchange
			temp=search_data[i]
			search_data[i]=search_data[largest]
			search_data[largest]=temp
			print("heapify:",i,search_data)
		heapify(search_data,largest)
#build function,to build up a big heap
def build_heap(search_data):
	length=len(search_data)
	mid=length/2
	mid=int(mid+1)
	for i in range(mid,0,-1):
		heapify(search_data,i)
if __name__=="__main__":
	test_data=[0,16,14,10,8,7,9,3,2,4,1]
	test_data1=[0,4,5,3,2,7,9,1,11,8,12]
	test_data2=[0,4,5,3,2,7,9,1,11,8,12]
	print("5's left son:",left(test_data,5))
	print("6's left son:",left(test_data,6))
	print("3's right son:",right(test_data,3))
	print("6's right son:",right(test_data,6))
	print("1's parent:",parent(test_data,1))
	print("11's parent:",parent(test_data,11))
	print("5's parent:",parent(test_data,5))
	print("test_data tree's heigth:",height(test_data,2))
	print("begin heapify the node 1:",test_data1)
	heapify(test_data1,1)
	print("begin build heap:",test_data2)
	build_heap(test_data2)
