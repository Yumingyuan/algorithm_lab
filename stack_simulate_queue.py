# -*- coding: utf-8 -*-
#利用两个stack来模拟一个队列
def delete_head(stack1,stack2):
	if len(stack2)<=0:
		while len(stack1)>0:
			data=stack1.pop()#取出stack1栈顶元素
			stack2.append(data)#将stack1的栈顶元素放入stack2
	if len(stack2)==0:#stack2栈内没东西
		print("Error! stack2 is empty")
		return
	head_num=stack2.pop()#取出stack2中最后入栈的元素
	print("headnum:",head_num)
if __name__=="__main__":
	stack1=["a","b","c","d"]#栈元素
	stack2=[]
	delete_head(stack1,stack2)#模拟队列操作
	delete_head(stack1,stack2)
	stack1.append("e")#往空的栈里再加些东西
	stack1.append("f")#往空的栈里再加些东西
	delete_head(stack1,stack2)#有效取队列头
	delete_head(stack1,stack2)#有效取队列头
	delete_head(stack1,stack2)#有效取队列头
	delete_head(stack1,stack2)#有效取对猎头
	delete_head(stack1,stack2)#无效取队列头（已经空了）
