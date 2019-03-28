# -*- coding: utf-8 -*-
#def joseph(people_list,out_list,m,n):
	#index=0
	#alive_num=m
	#while alive_num>0:
		#item=0
		#while item<n:
		#	if not out_list[item]:
			#	item=item+1
			#if item==n:
				#print("kill people:",people_list[index])
				#out_list[index]=False
				#alive_num-=1
			#index=(index+1)%m
def joseph(people_list,m,n):
	index=0
	for i in range(m-1):
		index=(index+n-1)%len(people_list)
		#index-=1
		print("kill:",people_list[index])
		del people_list[index]
		if index==-1:
			index=0
	print("Survive:",people_list)
if __name__=="__main__":
	m=int(input("m>"))
	n=int(input("n>"))
	people_list=[i for i in range(0,m)]
	#next_people=[(i+1)%m for i in range(0,m)]#构造循环链表，指向当前用户的下一个人的下标
	#print(people_list)
	joseph(people_list,m,n)
	#print(out_people_list)
