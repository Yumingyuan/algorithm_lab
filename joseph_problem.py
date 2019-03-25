# -*- coding: utf-8 -*-
def joseph(people_list,out_list,m,n):
	index=0
	alive_num=m
	while alive_num>0:
		item=0
		while item<n:
			if not out_list[item]:
				item=item+1
			if item==n:
				print("kill people:",people_list[index])
				out_list[index]=False
				alive_num-=1
			index=(index+1)%m
if __name__=="__main__":
	m=int(input("m>"))
	n=int(input("n>"))
	people_list=[i for i in range(0,m)]
	out_people_list=[False for i in range(0,m)]
	print(people_list)
	#print(out_people_list)
	joseph(people_list,out_people_list,m,n)
	print(out_people_list)
