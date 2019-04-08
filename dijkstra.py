# -*- coding: utf-8 -*-
#临接矩阵
map_data_list=[
[0,4,65535,2,65535],
[4,0,4,1,65535],
[65535,4,0,1,3],
[2,1,1,0,7],
[65535,65535,3,7,0]
]
min_length=[65535 for i in range(len(map_data_list))]#到已在被选中点集合中距离
selected=[False for i in range(len(map_data_list))]#判断节点是否已经被选中
if __name__=="__main__":
	chosen_node=0
	node_list=[chosen_node]#记录经过节点
	min_length[chosen_node]=chosen_node#设置初始节点
	selected[chosen_node]=True#节点被选中
	for i in range(0,len(map_data_list[0])):
		min_length[i]=min(min_length[i],map_data_list[0][i])#把0节点到外部节点的距离初始化一下
	for i in range(1,len(map_data_list)):#到最后一个节点(进行n-1次的局部dijkstra计算)
		most_min_value=65535
		for j in range(1,len(map_data_list)):#到最后一个节点
			if not selected[j] and min_length[j]<most_min_value:#没有被选择，且节点可达
				most_min_value=min_length[j]#局部最近的点和已选中节点集合的距离
				chosen_node=j
		selected[chosen_node]=True#将局部最近的点放入选中节点集合
		node_list.append(chosen_node)
		for j in range(1,len(map_data_list)):
			if min_length[j]>min_length[chosen_node]+map_data_list[chosen_node][j]:
				min_length[j]=min_length[chosen_node]+map_data_list[chosen_node][j]#更新到原点的最短距离
	print("min length:",min_length[len(min_length)-1])
	print("经过节点:",node_list)
