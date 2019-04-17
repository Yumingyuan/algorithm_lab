# -*- coding: utf-8 -*-
#临接矩阵,例子中是一个3种颜色可涂抹的情况
node_matrix=[[False,True,False,False],[True,False,True,True],[False,True,False,True],
[False,True,True,False]]
node_color=[0 for i in range(len(node_matrix))]#颜色向量
def iscollision(node_set,node_color,i,color):
	for j in range(i):#遍历已经着色的节点
		if node_set[i][j]==True and node_color[j]==color:#如果有一个j与i临接且着色一样，则不行！
			return True
	return False#没找到合适的j就没有颜色冲突
if __name__=="__main__":
	k=0
	while k>=0:
		while node_color[k]<=2:
			node_color[k]+=1#选择颜色
			if not iscollision(node_matrix,node_color,k,node_color[k]):
				if k==len(node_matrix)-1:#是个解
					print(node_color)
				else:
					k+=1#继续对下一个节点查找
		node_color[k]=0#重新选择
		k-=1#回溯
