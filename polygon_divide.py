# -*- coding: utf-8 -*-
#计算三角形周长
def triangle(edge_data,i,j,k):
	return edge_data[i][k]+edge_data[k][j]+edge_data[i][j]
#最优值计算函数
def calc_optimal(edge_data,edges_num):
	distance=[[0 for i in range(edges_num+1)] for j in range(edges_num+1)]#最优子权重
	for m in range(1,edges_num):#问题规模
		for i in range(0,edges_num-m):
			j=i+m
			#print("i:",i,"j:",j,"m:",m)
			min_num=65535
			min_k=0
			#print("distance:",distance)
			for k in range(i+1,j):
				#print("distance[i][k]",distance[i][k],distance[k][j],triangle(edge_data,i,j,k),i,j,k)
				if min_num>distance[i][k]+distance[k][j]+triangle(edge_data,i,j,k):
					min_num=distance[i][k]+distance[k][j]+triangle(edge_data,i,j,k)
					min_k=k
				distance[i][j]=min_num
	print(distance)
if __name__=="__main__":
	edge_data=[[0,14,25,27,10,11,24,16],
	[0,0,18,15,27,28,16,14],
	[0,0,0,19,14,19,16,10],
	[0,0,0,0,22,23,15,14],
	[0,0,0,0,0,14,13,20],
	[0,0,0,0,0,0,0,27],
	[0,0,0,0,0,0,0,0]]#上三角形
	edges=8#八边形
	calc_optimal(edge_data,edges)
