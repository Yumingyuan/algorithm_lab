def binary_expon(a,binary_list):
	result=1
	calc_num=a
	for i in range(0,len(binary_list)):#最低位不论是0还是1，值都应该是1
		if binary_list[i]==1:#先判断二进制值是不是1,如果是：则乘上被乘数
			result*=calc_num
		calc_num*=calc_num#重复平方法
	return result
if __name__=="__main__":
	binary_list=[0,1,1,1]#5^1110次方
	print("Result:",binary_expon(5,binary_list))
