def prim_aloorithm(edges,vertex_len):
	chosen=[i for  i in range(vertex_len)]
	lowcost=[i for  i in range(vertex_len)]
	choice=[i for i in range(vertex_len)]
	count_sum=0
	#init data set
	for i in range(0,vertex_len):
		chosen[i]=0
		lowcost[i]=edges[0][i]
	#begin calc
	chosen[0]=1 #chosen vertex 0
	print('choose vertex:0 the edges cost:0')
	for n in range(1,vertex_len):
		min_num=65535
		for m in range(0,vertex_len):
			if(chosen[m]==0 and lowcost[m]<min_num):
				min_num=lowcost[m]
				temp_select_vertex=m#find the most low cost vertex to add in the chosen set
		selected_vertex=temp_select_vertex
		count_sum=count_sum+lowcost[selected_vertex]
		print('choose vertex:%d the edges cost:%d'%(selected_vertex,lowcost[selected_vertex]))
		chosen[selected_vertex]=1
		choice[n]=selected_vertex
		#release the distance between the choosen vertex and unchoosen vertex
		for o in range(0,vertex_len):
			if(edges[selected_vertex][o]!=0 and edges[selected_vertex][o]!=65535 and edges[selected_vertex][o]<lowcost[o]):
				lowcost[o]=edges[selected_vertex][o]
	print("vertex choose sequence:",choice,"sum weight:",count_sum)				
if __name__=='__main__':
	edges=[[0,2,65535,4],[2,0,7,5],[65535,7,0,3],[4,5,3,0]]
	prim_aloorithm(edges,len(edges))
	
