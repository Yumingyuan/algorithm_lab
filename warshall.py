# -*- coding: utf-8 -*-
def warshall_calc(matrix):
	for edge in range(len(matrix)):
		for start_node_num in range(len(matrix)):
			for end_node_num in range(len(matrix)):
				if matrix[start_node_num][end_node_num]==True:#上一轮矩阵元素就是True时，不做操作
					pass

if __name__=="__main__":
	data_matrix_A=[[False,True,False,False],
											[False,False,False,True],
											[False,False,False,False],
											[True,False,True,False]]
	
