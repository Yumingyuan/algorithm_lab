# -*- coding: utf-8 -*-
def tekefirst(elem):
	return elem[1]#返回第1个元素		
def john_calc(job_nums,a,b,c):
	for i in range(job_nums):
		if a[i][1]>b[i][1]:
			key=b[i]
		else:
			key=a[i]
		print("key:",key)
		
if __name__=="__main__":
	a=[(0,2),(1,4),(2,3),(3,6),(4,1)]
	b=[(0,5),(1,2),(2,3),(3,1),(4,7)]
	sequence=[0 for i in range(len(a))]
	john_calc(len(a),a,b,sequence)
