# -*- coding: utf-8 -*-
data=[1,3,2,3,3,4,3,4]
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
if __name__=="__main__":
	reduce_one(data)
