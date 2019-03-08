import random
range_upper=20
length=10
list_unsort=random.sample(range(range_upper),length)
print('Before sort:',list_unsort)

gap=1
while gap<int(length/3):
	gap=gap*3+1

while gap>=1:
	print("current gap:",gap)
	for i in range(int(gap),int(length)):
		j=i
		temp=list_unsort[j]
		print("current compare num:",temp)
		while j>=gap and list_unsort[j]<list_unsort[j-gap]:
			list_unsort[j]=list_unsort[j-gap]
			list_unsort[j-gap]=temp
			j=j-gap
			print("medium unsort list:",list_unsort)
	gap=int(gap/3)
print('After sort:',list_unsort)
	
			
