# -*- coding: utf-8 -*-
def joseph(n):
	if n==1:
		return 1
	elif n%2==0:
		return 2*joseph(n/2)-1
	else:
		return 2*joseph((n-1)/2)+1
if __name__=="__main__":
	print("alive",joseph(5))
