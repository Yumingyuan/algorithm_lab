# -*- coding: utf-8 -*-
node_num=5
#node_num=4
#临接情况列表
node_matrix=[[False,True,True,True,False],[True,False,True,True,True],
[True,True,False,True,False],[True,True,True,False,True],[False,True,False,True,False]]
#node_matrix=[[False,True,False,False],[True,False,True,True],[False,True,False,True],
[False,True,True,False]]
def iscollision(node_set,node_color,i,color):
	for j in range(i):#遍历已经着色的节点
		if node_set[i][j]==True and node_color[j]==color:#如果有一个j与i临接且着色一样，则不行！
			return True
	return False#没找到合适的j就没有颜色冲突
def colorify(n):
	#node_set=[0 for i in range(n)]
	node_color=[0 for i in range(n)]#着色的向量
	color=1#初始颜色
	for i in range(node_num):#固定一个节点
		j=0
		while j<=color:
			j+=1
			if not iscollision(node_matrix,node_color,i,j):
				print("not collision",j)
				node_color[i]=j#着色
				#print("if",node_color)
				if i==node_num-1:
					print("node_color:",node_color)
					break
				break#跳出内层循环
			else:
				j+=1
				color+=1
				node_color[i]=color			
				#print("else:",node_color)
				if i==node_num-1:
					print("node_color:",node_color)	
					break
				break#跳出内层循环
	print("need",color,"num")
if __name__=="__main__":
	colorify(node_num)
