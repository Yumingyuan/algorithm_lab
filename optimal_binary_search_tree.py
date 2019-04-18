# -*- coding: utf-8 -*-
probablity=[0.1,0.2,0.4,0.3]
#生成节点个数+2行，节点个数+1列
solution=[[0 for i in range(len(probablity)+1)] for j in range(len(probablity)+2)]
result=[]
#对solution进行初始化
def initial():
	for i in range(len(probablity)):
		solution[i+1][i+1]=probablity[i]#查找“i+1”这个点的单个概率
