# -*- coding: utf-8 -*-
data=[1,3,2,3,3,4,3]
def reduce_one(data):
	num=data[0]
	count=0
	for i in data:
		if i==num:
			count+=1
		else:
			count-=1
			if count<0:
				num=i
				count=0
	print("majority item:",num)
def brute_force_middile(data):
	data.sort()
	middle_item=data[int(len(data)/2)]
	count=0
	for i in data:
		if middle_item==i:
			count+=1
	if count>=int(len(data)/2):
		print("majority item:",middle_item)
def brute_force(data):	
	for item1 in data:
		count=0
		for item2 in data:
			if item1==item2:
				count+=1
		if count>len(data)/2:
			return item1
def max_search(data):
	max_num=max(data)
	num_list=[0 for i in range(max_num+1)]
	for i in data:
		num_list[i]+=1
	max_num=max(num_list)
	for i in range(len(num_list)):
		if max_num==num_list[i]:
			print("majority item:",i)
	#print(num_list)
if __name__=="__main__":
	result=brute_force(data)
	print("majority item:",result)
	reduce_one(data)
	brute_force_middile(data)
	max_search(data)
