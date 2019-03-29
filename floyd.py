# -*- coding: utf-8 -*-
if __name__=="__main__":
	dis=[
	[999,2,999,999,2,10],
	[999,999,999,999,999,6],
	[999,999,999,999,999,1],
	[999,999,999,999,999,999],
	[999,999,1,999,999,999],
	[999,999,999,999,999,999]
	]
	vertex=[]
	for i in range(len(dis)):
		for j in range(len(dis)):
			for k in range(len(dis)):
				if dis[i][j]>dis[i][k]+dis[k][j]:
					dis[i][j]=dis[i][k]+dis[k][j]
	print(dis)
