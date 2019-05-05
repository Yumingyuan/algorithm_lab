# -*- coding: utf-8 -*-
#构造最优解
def print_solution(i,j,optim_k):#打印i->k->j三角形
	if i+1==j:#如果不能形成三角形则返回
		return
	else:
		print("(V"+str(i+1)+"V"+str(optim_k[i][j]+1)+"V"+str(j+1)+")",end='')
		print_solution(i,optim_k[i][j],optim_k)#递归多边形打印(Vi->Voptim_k[i][j])
		print_solution(optim_k[i][j],j,optim_k)#递归打印(Voptim_k[i][j]->Vj)
#计算并返回三角形周长(i,j,k这三个点形成的)
def triangle(edge_data,i,j,k):
	#print("i",i,"j",j,"k",k)
	#print("triangle",edge_data[i][k],edge_data[k][j],edge_data[i][j])
	return edge_data[i][k]+edge_data[k][j]+edge_data[i][j]
#最优值计算函数
def calc_optimal(edge_data,edges_num):
	distance=[[0 for i in range(edges_num)] for j in range(edges_num)]#最优子权重
	optim_k=[[0 for i in range(edges_num)] for j in range(edges_num)]#最优的分割点
	for m in range(1,edges_num):#问题规模
		for i in range(0,edges_num-m):
			j=i+m
			#print("i:",i,"j:",j,"m:",m)
			min_num=65535
			min_k=0
			#print("distance:",distance)
			for k in range(i+1,j):#k是断开位置从i+1到j-1
				#print("distance[i][k]:",distance[i][k],"distance[k][j]",distance[k][j],"triangle(i,j,k)",triangle(edge_data,i,j,k),i,j,k)
				#print("triangle",edge_data[i][k],edge_data[k][j],edge_data[i][j],i,j,k)
				if min_num>distance[i][k]+distance[k][j]+triangle(edge_data,i,j,k):
					min_num=distance[i][k]+distance[k][j]+triangle(edge_data,i,j,k)
					min_k=k
				distance[i][j]=min_num
				#print("update dis",distance)
				optim_k[i][j]=min_k	
				#print("update optimum",optim_k)		
	print("optimum weight:",distance[0][edges_num-1])
	print("optimal divide solution:",end='')
	print_solution(0,7,optim_k)#构造最优结果函数调用
if __name__=="__main__":
	edge_data=[[0,14,25,27,10,11,24,16],
	[0,0,18,15,27,28,16,14],
	[0,0,0,19,14,19,16,10],
	[0,0,0,0,22,23,15,14],
	[0,0,0,0,0,14,13,20],
	[0,0,0,0,0,0,15,18],
	[0,0,0,0,0,0,0,27],
	[0,0,0,0,0,0,0,0]]#上三角形
	edges=8#八边形
	calc_optimal(edge_data,edges)
