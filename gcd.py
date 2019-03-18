def gcd(m,n):
	while n!=0:
		r=m%n
		m=n
		n=r
	return m
if __name__=="__main__":
	print(gcd(1995,615))
