def horner(data_list,x):
	p=data_list[len(data_list)-1]#取多项式中次数最高项系数
	for i in range(len(data_list)-2,-1,-1):#将每个加数（实际上也是系数）进行相加，由于要访问数组的0项元素，所以边界是-1（python range特性所造成的）
		p=p*x+data_list[i]#计算:x*p+num
	return p#返回结果
if __name__=="__main__":
	data_set=[-5,1,3,-1,2]
	print("calc result:",horner(data_set,3))#函数调用
