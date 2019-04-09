# -*- coding: utf-8 -*-
def joseph(n):
	if n==1:#仅剩1人
		return 1
	elif n%2==0:#偶数情况
		return 2*joseph(n/2)-1
	else:#奇数情况
		return 2*joseph((n-1)/2)+1
if __name__=="__main__":
	print("alive:",joseph(5))#函数调用
