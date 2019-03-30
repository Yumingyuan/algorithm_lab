# -*- coding: utf-8 -*-
def make_set(x):
	p=[i for i in range(0,x)]#生成边集合
	rank=[0 for i in range(0,x)]#生成kruskal的长度集合
	return p,rank
def find_set(search_set,x):
	if x>len(search_set)-1:#当查找的数据超过树的大小，则不符合要求
		return -1
	return search_set[x]#返回查找结果
def union(search_set,p,q):#合并操作
	pid=p
	qid=q
	if pid==qid:
		return	
	for i in range(0,len(search_set)):
		if search_set[i]==pid:
			search_set[i]=search_set[qid]
	#print("after union:",search_set)
def kruskal_prim(sorted_list,vertex_set_list):
	for i in range(0,len(sorted_list)):
		if find_set(vertex_set_list,sorted_list[i][0])!=find_set(vertex_set_list,sorted_list[i][1]):
			union(vertex_set_list,sorted_list[i][0],sorted_list[i][1])
			print("choose edge's weight",sorted_list[i][2])
def tekethird(elem):
	return elem[2]#返回第三个元素			
if __name__=='__main__':
	edges=[[0,2,65535,4],[2,0,7,5],[65535,7,0,3],[4,5,3,0]]
	need_sort_edges=[]
	#init the vertex set
	vertex_set,rank=make_set(len(edges))#创建集合
	for i in range(0,len(edges)):
		for j in range(0,len(edges[i])):
			#排除无效边:不联通的和加入后形成环路的不能加入
			if edges[i][j]!=65535 and edges[i][j]!=0 and (j,i,edges[i][j]) not in need_sort_edges:
				#make the two vertex and the edge the two vertex associated with in the list "need_sort_edges"
				need_sort_edges.append((i,j,edges[i][j]))
	need_sort_edges.sort(key=tekethird)#sort by third element
	print("after sort:",need_sort_edges)#now the list is sorted
	kruskal_prim(need_sort_edges,vertex_set)
	#print("vertex_set:",vertex_set)
