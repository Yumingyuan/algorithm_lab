# -*- coding: utf-8 -*-
probablity=[0.1,0.2,0.4,0.3]
#生成节点个数+2行，节点个数+1列
solution=[[0 for i in range(len(probablity)+1)] for j in range(len(probablity)+2)]
result=[[0 for i in range(len(probablity)+1)] for j in range(len(probablity)+1)]
#对solution进行初始化
def initial():
	for i in range(len(probablity)):
		solution[i+1][i+1]=probablity[i]#查找“i+1”这个点的单个概率
	print("after init",solution)
def calc_optimal():
	min_k=0
	for dimension in range(1,len(probablity)):
		for i in range(1,len(probablity)-dimension):
			j=i+dimension
			min_val=65535
			for k in range(i,j+1):
				if solution[i][k-1]+solution[k+1][j]<min_val:
					min_val=solution[i][k-1]+solution[k+1][j]#更新最优值
					min_k=k
			result[i][j]=min_k#更新最优断开位置k
			sum_prob=probablity[i-1]
			for index in range(i,j):
				print("add",probablity[index])
				sum_prob+=probablity[index]
			solution[i][j]+=sum_prob
	print(solution)
	print(result)
if __name__=="__main__":
	initial()#调用初始化函数
	calc_optimal()
