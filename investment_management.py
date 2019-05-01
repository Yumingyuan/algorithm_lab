# -*- coding: utf-8 -*-
#动态规划计算最优值函数
def calc_optimal(project_data,project_num,money):
	#计算最优投资额的向量
	selection_income=[[0 for i in rang(money+1)] for j in range(project_num+1)]#多生成一个投资8万也会盈利0元的项目作为边缘的计算变量
	#计算过程，反向计算
	for i in range(project_num-1,-1,-1):#从2号项目到0号项目
		for j in range(0,money+1):#从0万到8万,决定投资i项目所花的资金
			max_num=0#小值
			if max_num<project_data[i][j]+selection_income[i+1][money-j]:
				max_num=project_data[i][j]+selection_income[i+1][money-j]#实时最优值
if __name__=="__main__":
	#投资金额及收回的金额，下标为投资金额，盈利为数据
	project_num=3
	investment_money=8
	projec_data=[
	[0,5,15,40,80,90.95.98,100],
	[0,5,15,40,60,70,73,74,75],
	[0,4,26,40,45,50,51,52,53]]
