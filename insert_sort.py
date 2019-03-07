import random
range_upper=20
length=10
list_unsort=random.sample(range(range_upper),length)
print('Before sort:',list_unsort)

for i in range(1,length):
	j=i
	temp_num=list_unsort[j]#to insert's num compare from i-1 to 0
	while j>0 and list_unsort[j-1]>temp_num:
		list_unsort[j]=list_unsort[j-1]
		j=j-1
		print(i,j)
	list_unsort[j]=temp_num
print('After sort:',list_unsort)
	
