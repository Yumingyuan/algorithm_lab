# -*- coding: utf-8 -*-
probablity=[0.1,0.2,0.4,0.3]
#生成节点个数+2行，节点个数+1列
solution=[[0 for i in range(len(probablity)+1)] for j in range(len(probablity)+2)]
result=[[0 for i in range(len(probablity)+1)] for j in range(len(probablity)+1)]
def print_result(i,j):
	if i==j:
		print("node"+str(i),end='')
	else:
		print("(",end='')
		print_result(i,result[i][i])
		print_result(result[i][i]+1,j)
		print(")",end='')
#对solution进行初始化
def initial():
	#遍历节点查找的可能概率
	for i in range(len(probablity)):
		solution[i+1][i+1]=probablity[i]#查找“i+1”这个点的单个概率
		result[i+1][i+1]=i+1
	print("After init",result)
def calc_optimal():
	min_k=0
	for dimension in range(1,len(probablity)):
		for i in range(1,len(probablity)-dimension+1):
			j=i+dimension
			min_val=65535
			for k in range(i,j+1):#决定谁当父节点
				if solution[i][k-1]+solution[k+1][j]<min_val:#如果小于当前最优值，更新
					min_val=solution[i][k-1]+solution[k+1][j]#更新最优值
					min_k=k
			solution[i][j]=min_val#更新最优值
			result[i][j]=min_k#更新最优断开位置k
			sum_prob=0
			for index in range(i-1,j):#从i-1加到j-1把所有节点的查找概率加入
				sum_prob+=probablity[index]#累计相加
			solution[i][j]+=sum_prob
	print(solution[1][len(probablity)])
	#print("result",result)
	print_result(1,4)#构造结果
if __name__=="__main__":
	initial()#调用初始化函数
	calc_optimal()
