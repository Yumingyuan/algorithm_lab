# -*- coding: utf-8 -*-
def joseph(people_list,m,n):
	index=0
	for i in range(m-1):#找到m-1项，进行kill
		index=(index+n-1)%len(people_list)#报数
		#index-=1
		print("kill:",people_list[index])
		#print("before kill index",index)
		del people_list[index]#将当前的索引对应的元素删除
		#print("after kill index",index)
	print("Survive:",people_list)#最后剩下一项，输出活着
#def joseph_iter(people_list,next_people,m,n):
	#alive=m
	#index=-1
	#while alive>0:
		#for i in range(n-1):
			#index=next_people[index]
		#print("kill",people_list[(index+1)%m])
		#alive-=1
		#next_people[index]=next_people[next_people[index]]
		#print("current index:",index,next_people)
if __name__=="__main__":
	m=int(input("m>"))
	n=int(input("n>"))
	people_list=[i for i in range(0,m)]
	next_people=[(i+1)%m for i in range(0,m)]#构造循环链表，指向当前用户的下一个人的下标
	#joseph_iter(people_list,next_people,m,n)
	#print(people_list)
	joseph(people_list,m,n)
	#print(out_people_list)
