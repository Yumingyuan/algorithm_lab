# -*- coding: utf-8 -*-
def binominal_calc(n,k):
	bin_list=[[0 for i in range(k+1)] for j in range(n+1)]
	for i in range(n+1):#从0遍历至n
		for j in range(k+1):#从0遍历至k
			if j==0 or j==i:
				bin_list[i][j]=1#如果是c(n,0)或c(n,n)则结果为1
			else:
				bin_list[i][j]=bin_list[i-1][j-1]+bin_list[i-1][j]#反之则动态规划，使用之前计算的结果进行计算
	print(bin_list[n][k])
if __name__=="__main__":
	binominal_calc(3,2)#函数调用
