# -*- coding: utf-8 -*-
import sys
def reverselist(need_reverse_list):#将列表进行反转
	i=0
	while need_reverse_list[i]==0:
		i+=1
	res=''
	for j in range(i,len(need_reverse_list)):
		res+=str(need_reverse_list[j])
	return res
def multi(stra,strb):
	list_a=list(stra)#对字符串创建成列表
	list_b=list(strb)
	print(list_a,list_b)
	length_a=len(list_a)
	length_b=len(list_b)
	result_list=[0 for i in range(length_a+length_b)]#创建一个长度等于两个乘数长度总和的列表
	for i in range(length_a):
		for j in range(length_b):
			result_list[length_a-i-1+length_b-j-1]+=int(list_a[i])*int(list_b[j])#逆序存入
			print(i,j,result_list)
	for i in range(len(result_list)-1):
		if result_list[i]>=10:#结果大于10
			result_list[i+1]+=result_list[i]/10#大于10则进位
			result_list[i]=result_list[i]%10#把当前位加入当前位置
	return reverselist(result_list[::-1])#反转列表：result_list[::-1]就相当于已经对result_list反转了
if __name__=="__main__":
	if len(sys.argv)!=3:#不提交参数则失败
		print("please input 2 argument [Bigint1] [Bigint2]")
		exit()
	optnum_a=sys.argv[1]
	optnum_b=sys.argv[2]
	print("result:",multi(optnum_a,optnum_b))
