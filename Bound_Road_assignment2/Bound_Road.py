# -*- coding: utf-8 -*-
#上界：当前已经符合要求的最小解
#下界：没有金额约束的最优最短路
import copy
def read_file():#读取文件函数,返回公路长度和养护费用列表
	f1_list=[]#公路联通情况和每段公路的长度
	f2_list=[]#公路养护费用
	f1=open("m1.txt","r")
	f2=open("m2.txt","r")
	for lines in f1:
		ls=lines.strip('\n').split('\t')#去掉结尾的\n并把每行内容按\t分开
		ls=[int(num) for num in ls]#字符串转为int数!!!!!!!!!技巧
		f1_list.append(ls)
	for lines in f2:
		ls=lines.strip('\n').split('\t')#去掉结尾的\n并把每行内容按\t分开
		ls=[int(num) for num in ls]#字符串转为int数
		f2_list.append(ls)
	return f1_list,f2_list
def floyd(length_list):#floyd算法
	update_length_list=[[0 for i in range(len(length_list[0]))] for i in range(len(length_list))]#生成一个与length_list大小匹配的二维列表，为后续深拷贝打基础
	update_length_list=copy.deepcopy(length_list)#把length_list深度拷贝到update_length_list
	for i in range(len(update_length_list)):
		for j in range(len(update_length_list)):
			for k in range(len(update_length_list)):
				if update_length_list[i][j]>update_length_list[i][k]+update_length_list[k][j]:
					update_length_list[i][j]=update_length_list[i][k]+update_length_list[k][j]
	return update_length_list#返回经过松弛的列表
if __name__=="__main__":
	length_list,value_list=read_file()
	#print("Before soft:",value_list)
	min_list_length=floyd(length_list)
	min_cost_length=floyd(value_list)
	#print("After soft:",min_cost_length)
