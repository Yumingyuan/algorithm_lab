# -*- coding: utf-8 -*-
def read_file():
	f1_list=[]#公路联通情况和每段公路的长度
	f2_list=[]#公路养护费用
	f1=open("m1.txt","r")
	
	for lines in f1:
		ls=lines.strip('\n').split('\t')#去掉结尾的\n并把每行内容按\t分开
		f1_list.append(ls)
	print(f1_list)
if __name__=="__main__":
	read_file()
