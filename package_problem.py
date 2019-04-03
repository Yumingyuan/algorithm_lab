# -*- coding: utf-8 -*-
def knapsack_dynamic(wl,price,length,m,x):
	for i in range(1,length+1):#遍历1-n这些货物
		for j in range(1,m+1):
			optp[i][j]=optp[i-1][j]
			if(j>=wl[i]) and (optp[i-1][j-wl[i]]+price[i]>optp[i-1][j]):
				optp[i][j]=optp[i-1][j-wl[i]]+price[i]
	j=m
	for i in range(length,0,-1):
		if optp[i][j]>optp[i-1][j]:
			x[i]=True
			j=j-wl[i]
	result=optp[length][m]
	return result
if __name__=="__main__":
	weight_list=[0,2,2,6,5,4]#0元素无用
	price=[0,6,3,5,4,6]#0号元素 无用
	length=len(weight_list)-1#有多少个货物可装
	m=10#背包可承载的重量
	x=[False for raw in range(length+1)]#决定要装载哪些货物
	optp=[[0 for col in range(m+1)] for raw in range(length+1)]#二维列表生成式
	print("max num is:"+str(knapsack_dynamic(weight_list,price,length,m,x)))
	print("solution:",x[1:])
