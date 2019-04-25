# -*- coding: utf-8 -*-
def russia_multi(opt1,opt2):
	result_sum=0#需要返回的结果
	while opt1!=0:#由于int(1/2)==0，所以当opt1为0,已经计算出结果
		if opt1%2==1:
			result_sum+=opt2#每当遇到opt1是奇数时，则将结果加opt2
		opt1=int(opt1/2)#每次将opt1进行折半，向下取整
		opt2=opt2*2#每次将opt2变为原来的两倍
	return result_sum
if __name__=="__main__":
	opt1=int(input("please input opt num 1:"))#输入参数1
	opt2=int(input("please input opt num 2:"))#输入参数2
	print("result:",russia_multi(opt1,opt2))#打印计算结果
