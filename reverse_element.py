# -*- coding: utf-8 -*-
items=[1,2,0,4,3,2,6]
queue=[]
count=0
for i in range(len(items)):
	for j in range(i,len(items)):
		if items[i]>items[j]:
			count+=1
			queue.append((items[i],items[j]))
print("count result:",count)
print("result:",queue)
