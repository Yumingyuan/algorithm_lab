# -*- coding: utf-8 -*-
chain=[30,35,15,5,10,20,25]#30*35,35*15,15*5,5*10,10*20,20*25共6个矩阵
matrix_num=len(chain)-1#共几个矩阵参与相乘
matrix_value=[[0 for i in range(matrix_num)] for j in range(matrix_num)]#生成n*n的矩阵保存相乘次数
matrix_solution=[[0 for i in range(matrix_num)] for j in range(matrix_num)]#生成n*n的矩阵保存加括号位置
def matrix_chain_order():
	#当i=1，j=0,k从0-1
	for i in range(1,matrix_num):#i负责关注的是运算规模，第一轮是计算2个矩阵连乘的状态
		for j in range(i-1,-1,-1):#j负责取出每一个矩阵的行数
			matrix_value[j][i]=655350000000000#非常大的值，确保乘积不会超过
			for k in range(j,i):#选择在哪里断开括号j<=k<i
				if matrix_value[j][k]+matrix_value[k+1][i]+chain[j]*chain[k+1]*chain[i+1]<matrix_value[j][i]:
					matrix_value[j][i]=matrix_value[j][k]+matrix_value[k+1][i]+chain[j]*chain[k+1]*chain[i+1]
					matrix_solution[j][i]=k#最优断开位置
				print("k",k,i,j)
def print_solution(i,j):#从i打印到j
	if i==j:#索引到单个矩阵时，直接打印
		print("A"+str(i),end='')#end参数保证print不会换行
	else:
		print("(",end='')#加左括号
		print_solution(i,matrix_solution[i][j])#从0到分割矩阵0-最后一个矩阵的分割矩阵处
		print_solution(matrix_solution[i][j]+1,j)#从分割矩阵的下一个矩阵进行打印，知道最后一个矩阵
		print(")",end='')#加右括号，一次递归结束
if __name__=="__main__":
	matrix_chain_order()
	print("cost:",matrix_value[0][matrix_num-1])#打印0到num-1总耗费
	print(matrix_solution)
	print_solution(0,matrix_num-1)#从0-5共6个矩阵相乘的结果
