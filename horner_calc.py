def horner(data_list,x):
	p=data_list[0]#取多项式中次数最高项系数
	for i in range(1,len(data_list)):
		p=p*x+data_list[i]#计算:b*x+c
	return p
if __name__=="__main__":
	data_set=[2,-1,3,1,-5]
	print("calc result:",horner(data_set,3))#函数调用
