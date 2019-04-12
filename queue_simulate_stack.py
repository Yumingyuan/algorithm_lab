# -*- coding: utf-8 -*-
#插入函数insertinqueue确保只有一个队列中有元素
def insertinqueue(queue1,queue2,item):
	#当queue1为空，则往queue2的队尾加入东西
	if len(queue1)==0:
		#加入新加入元素
		queue2.append(item)
	else:#反之queue2为空，则往queue1的队尾加入东西
		queue1.append(item)
#删除队尾元素函数delete_tail，把非空队列的0-(len-1)元素放入空队列
def delete_tail(queue1,queue2):
	if len(queue1)==0 and len(queue2)==0:#当栈为空
		return
	#当队列1中无元素时将queue2中的元素从队首移除len(queue2)-1个，并输出queue2中的剩下的元素
	if len(queue1)==0:
		while len(queue2)!=1:
			data=queue2.pop(0)#获得队首元素
			queue1.append(data)
		print("item pop",queue2.pop(0))#将移除len-1个队首元素的queue2中剩下的元素输出
	#当队列2中无元素时将queue1中的元素从队首移除len(queue1)-1个，并输出queue1中的剩下的元素
	elif len(queue2)==0:
		while len(queue1)!=1:
			data=queue1.pop(0)#获得队首元素
			queue2.append(data)
		print("item pop",queue1.pop(0))#将移除len-1个队首元素的queue1中剩下的元素输出
	else:
		pass
if __name__=="__main__":
	queue1=["a","b","c","d","e"]
	queue2=[]
	#删除尾部节点函数调用
	delete_tail(queue1,queue2)
	insertinqueue(queue1,queue2,"f")
	delete_tail(queue1,queue2)
	delete_tail(queue1,queue2)
	delete_tail(queue1,queue2)
	delete_tail(queue1,queue2)
	insertinqueue(queue1,queue2,"g")
	insertinqueue(queue1,queue2,"h")
	delete_tail(queue1,queue2)
	delete_tail(queue1,queue2)#正常弹出
	delete_tail(queue1,queue2)#正常弹出
	delete_tail(queue1,queue2)#此时栈为空，无效
