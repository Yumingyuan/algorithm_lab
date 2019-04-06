# -*- coding: utf-8 -*-
chain=[30,35,15,5,10,20,25]#30*35,35*15,15*5,5*10,10*20,20*25共6个矩阵
matrix_num=len(chain)-1#共几个矩阵参与相乘
matrix_value=[[0 for i in range(matrix_num)] for j in range(matrix_num)]#生成n*n的矩阵保存相乘次数
matrix_solution=[[0 for i in range(matrix_num)] for j in range(matrix_num)]#生成n*n的矩阵保存加括号位置
def matrix_chain_order():
	for i in range(1,matrix_num):#i负责取出每一个矩阵的列数
		for j in range(i-1,-1,-1):#j负责取出每一个矩阵的行数
			matrix_value[j][i]=65535#大值
			for k in range(j,i):#选择在哪里断开括号
				if matrix_value[j][k]+matrix_value[k+1][i]+chain[j]*chain[k+1]*chain[i+1]<matrix_value[j][i]:
					matrix_value[j][i]=matrix_value[j][k]+matrix_value[k+1][i]+chain[j]*chain[k+1]*chain[i+1]
					matrix_solution[j][i]=k#最优断开位置
def print_solution():
	pass
if __name__=="__main__":
	matrix_chain_order()
	print(matrix_value)
	print(matrix_solution)
