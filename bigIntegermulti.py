import sys
def reverselist(need_reverse_list):
	i=0
	while need_reverse_list[i]==0:
		i+=1
	res=''
	for j in range(i,len(need_reverse_list)):
		res+=str(need_reverse_list[j])
	return res
def multi(stra,strb):
	list_a=list(stra)
	list_b=list(strb)
	print(list_a,list_b)
	length_a=len(list_a)
	length_b=len(list_b)
	result_list=[0 for i in range(length_a+length_b)]
	for i in range(length_a):
		for j in range(length_b):
			result_list[length_a-i-1+length_b-j-1]+=int(list_a[i])*int(list_b[j])
	for i in range(len(result_list)-1):
		if result_list[i]>=10:
			result_list[i+1]+=result_list[i]/10
			result_list[i]=result_list[i]%10
	return reverselist(result_list[::-1])
if __name__=="__main__":
	if len(sys.argv)!=3:
		print("please input 2 argument [Bigint1] [Bigint2]")
		exit()
	optnum_a=sys.argv[1]
	optnum_b=sys.argv[2]
	print("result:",multi(optnum_a,optnum_b))
