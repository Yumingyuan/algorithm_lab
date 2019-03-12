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
test_data=[0,16,14,10,8,7,9,3,2,4,1]
print(left(test_data,5))
print(left(test_data,6))
print(right(test_data,3))
print(right(test_data,6))
