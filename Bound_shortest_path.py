# -*- coding: utf-8 -*-
map_data_list=[
[0,4,65535,2,65535],
[4,0,4,1,65535],
[65535,4,0,1,3],
[2,1,1,0,7],
[65535,65535,3,7,0]]
length=[0,65535,65535,65535,65535]
Queue=[]#用于进行分支的队列
def branch(matrix,v0):
	Queue.append(v0)
	current_vertex=matrix[0]
	while len(Queue)!=0:
		head=Queue[0]#取出当前队手需要搜索的节点下标
		for i in range(len(current_vertex)):
			if length[head]+current_vertex[i]
	
