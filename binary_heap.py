def left(search_data,i):
	set_length=len(search_data)
	if i==0 or 2*i>set_length:
		return
	else:
		return search_data[2*i]
def right(search_data,i):
	set_length=len(search_data)
	if i==0 or 2*i+1>set_length:
		return
	else:
		return search_data[2*i+1]
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
test_data=[0,16,14,10,8,7,9,3,2,4,1]
print("5's left son:",left(test_data,5))
print("6's left son:",left(test_data,6))
print("3's right son:",right(test_data,3))
print("6's right son:",right(test_data,6))
print("1's parent:",parent(test_data,1))
print("11's parent:",parent(test_data,11))
print("5's parent:",parent(test_data,5))
