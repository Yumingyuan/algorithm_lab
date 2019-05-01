# -*- coding: utf-8 -*-
#构造投资额
def calc_invest_option(project_num,money,optimum_investment):
	investment_list=[]
	investment_list.append(optimum_investment[0][8])#地一个项目投资额
	cur_money=money-investment_list[0]#剩余资金
	for i in range(1,project_num):
		investment_list.append(optimum_investment[i][cur_money])
		cur_money-=investment_list[i]
	for i in range(len(investment_list)):
		print("project"+str(i)+":"+investment_list[i])
#动态规划计算最优值函数
def calc_optimal(project_data,project_num,money):
	#计算最优投资额的向量
	selection_income=[[0 for i in range(money+1)] for j in range(project_num+1)]#多生成一个投资8万也会盈利0元的项目作为边缘的计算变量
	#记录最优投资额的向量
	optimum_investment=[[0 for i in range(money+1)] for j in range(project_num+1)]
	#计算过程，反向计算
	for i in range(project_num-1,-1,-1):#从2号项目到0号项目
		for j in range(0,money+1):#从0万到8万,决定投资i及i以后项目所花的资金
			max_num=0#小值
			opti_invest_cur=0#记录当前阶段最优投资额
			opti_invest_next=0#记录后续项目由于本阶段投资剩余投资金额数目
			for k in range(0,j+1):#决定投资i项目注入资金
				#print("k:",k,j,i)
				if max_num<project_data[i][k]+selection_income[i+1][j-k]:
					max_num=project_data[i][k]+selection_income[i+1][j-k]#实时最优值
					opti_invest_cur=k
					opti_invest_next=j-k
			selection_income[i][j]=max_num
			optimum_investment[i][j]=opti_invest_cur#记录对于i项目最优投资额
	print("optimun income:",selection_income[0][money])		
	calc_invest_option(project_num,money,optimum_investment)	
if __name__=="__main__":
	#投资金额及收回的金额，下标为投资金额，盈利为数据
	project_num=3
	investment_money=8
	project_data=[
	[0,5,15,40,80,90,95,98,100],
	[0,5,15,40,60,70,73,74,75],
	[0,4,26,40,45,50,51,52,53],
	[0,0,0,0,0,0,0,0,0]]
	calc_optimal(project_data,project_num,investment_money)
