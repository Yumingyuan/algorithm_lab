# -*- coding: utf-8 -*-
node_num=5
node_matrix=[[False,True,True,True,False],[True,False,True,True,True],
[True,True,False,True,False],[True,True,True,False,True],[False,True,False,True,False]]
def iscollision(node_set,node_color,i,color):
	for j in range(i):#遍历从i出发的所有临接节点j
		if node_set[i][j]==True and node_color[j]==color:#如果有一个j与i临接且着色一样，则不行！
			return True
	return False#没找到合适的j就没有颜色冲突
def colorify(n):
	node_set=[0 for i in range(n)]
	node_color=[0 for i in range(n)]#着色的向量
	color=1#初始颜色
	for i in range(node_num):#固定一个节点
		for j in range(1,color+1):#遍历颜色
			print("color can use:",color)
			if not iscollision(node_matrix,node_color,i,j):
				node_color[i]=j#着色
				if i==node_num-1:
					print("node_color:",node_color)
			else:
				color+=1
				node_color[i]=color
				print("color",color)
				if i==node_num-1:
					print("node_color:",node_color)
	print("need",color,"num")
if __name__=="__main__":
	colorify(node_num)
