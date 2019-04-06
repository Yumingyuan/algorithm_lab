# -*- coding: utf-8 -*-
chain=[30,35,15,5,10,20,25]#30*35,35*15,15*5,5*10,10*20,20*25共6个矩阵
matrix_num=len(chain)-1#共几个矩阵参与相乘
matrix_value=[[0 for i in range(n)] for j in range(n)]#生成n*n的矩阵保存相乘次数
matrix_solution=[[0 for i in range(n)] for j in range(n)]#生成n*n的矩阵保存加括号位置
def matrix_chain_order(data_list):
	for i in range(1,matrix_num):#i负责取出每一个矩阵的列数
		for j in range(i-1,-1,-1):
			m[j][i]=65535#大值
			for k in range(j,i):
				if m[j][k]+m[k+1][i]+chain[j]*chain[k+1]*chain[i+1]:
