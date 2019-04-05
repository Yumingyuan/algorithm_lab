# -*- coding: utf-8 -*-
#临接矩阵
map_data_list=[
[65535,1,4,65535,65535,65535,65535,65535,65535,65535],#0号节点
[65535,65535,65535,4,2,65535,65535,65535,65535,65535],#1号节点
[65535,65535,65535,65535,65535,1,1,65535,65535,65535],#2号节点
[65535,65535,65535,65535,65535,65535,65535,4,65535,65535],#3号节点
[65535,65535,65535,65535,65535,65535,65535,5,65535,65535],#4号节点
[65535,65535,65535,65535,65535,65535,65535,65535,3,65535],#5号节点
[65535,65535,65535,65535,65535,65535,65535,65535,6,65535],#6号节点
[65535,65535,65535,65535,65535,65535,65535,65535,65535,2],#7号节点
[65535,65535,65535,65535,65535,65535,65535,65535,65535,1],#8号节点
[65535,65535,65535,65535,65535,65535,65535,65535,65535,65535]#9号节点
]
#从i节点出发到终点的最短距离
cost_list=[0 for i in range(len(map_data_list))]
path_list=[0 for i in range(len(map_data_list))]
for i in range(len(map_data_list)-2,-1,-1):#i从8遍历到0
	min_cost=65535
	for j in range(len(map_data_list)-1,i,-1):#j从9遍历到i+1
		if map_data_list[i][j]!=65535:
			if cost_list[j]+map_data_list[i][j]<min_cost:
				#print("i,j in if",i,j,map_data_list[i][j],cost_list[j]+map_data_list[i][j])
				min_cost=cost_list[j]+map_data_list[i][j]#从j到最终节点距离加上j到i的距离，越小越选择
				min_node=j
	cost_list[i]=min_cost#对于i，这是当前到最后的节点的最短距离
	path_list[i]=min_node#通过j节点，使得i到最后的节点距离最短
	#print("i,j",i,j,cost_list,path_list)	
print("从0点出发到9号节点距离:",cost_list[0])
print("path:",0)
i=path_list[0]
while i!=0:
	print("path:",i)
	i=path_list[i]
