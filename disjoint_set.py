def make_set(x):
	p=[i for i in range(0,x)]
	print(p)
	return p
def find_set(search_set,x):
	if x>len(search_set)-1:
		return -1
	return search_set[x]
def union(search_set,p,q):
	pid=p
	qid=q
	if pid==qid:
		return	
	for i in range(0,len(search_set)):
		if search_set[i]==pid:
			search_set[i]=search_set[qid]
	print("after union:",search_set)
if __name__=='__main__':
	gen_set=make_set(10)
	info=input('>[num1] [num2]:')
	while len(info):
		split_info=info.split(' ')
		union(gen_set,int(split_info[0]),int(split_info[1]))
		info=input('>[num1] [num2]:')
