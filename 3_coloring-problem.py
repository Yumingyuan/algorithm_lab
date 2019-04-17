# -*- coding: utf-8 -*-
#临接矩阵,例子中是一个4种颜色可涂抹的情况
node_matrix=[[False,True,True,True,False],[True,False,True,True,True],
[True,True,False,True,False],[True,True,True,False,True],[False,True,False,True,False]]
#初始化填色列表,颜色为0
node_color=[0 for i in range(len(node_matrix))]
def iscollision(node_set,node_color,i,color):
	for j in range(i):#遍历已经着色的节点
		if node_set[i][j]==True and node_color[j]==color:#如果有一个j与i临接且着色一样，则不行！
			return True
	return False#没找到合适的j就没有颜色冲突
def graphcolor(procedure):
	if procedure==len(node_matrix):
		print("resolution:",node_color)
	else:
		for color in range(1,5):#4着色
			node_color[procedure]=color
			if not iscollision(node_matrix,node_color,procedure,color):
				graphcolor(procedure+1)
if __name__=="__main__":
	graphcolor(0)
