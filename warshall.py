# -*- coding: utf-8 -*-
def printmatrix(matrix):
	for matrix_row in range(len(matrix)):
		print(matrix[matrix_row])
def warshall_calc(matrix):
	for release_node_num in range(len(matrix)):
		for start_node_num in range(len(matrix)):
			for end_node_num in range(len(matrix)):
				if matrix[start_node_num][end_node_num]==True:#上一轮矩阵元素就是True时，不做操作
					pass
				#当当前的中间节点能够连接startnode和endnode时，设置为true
				elif matrix[start_node_num][release_node_num]==True and matrix[release_node_num][end_node_num]==True:
					matrix[start_node_num][end_node_num]=True
				else:
					pass
		print("matrix:",release_node_num+1)
		printmatrix(matrix)
if __name__=="__main__":
	data_matrix_A=[[False,True,False,False],
											[False,False,False,True],
											[False,False,False,False],
											[True,False,True,False]]
	print("matrix:",0)
	printmatrix(data_matrix_A)
	warshall_calc(data_matrix_A)
