# -*- coding: utf-8 -*-
class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
if __name__=="__main__":
	node2=Node("data1",None)
	node3=Node("data2",node2)
	print(node3.next.data)#访问node3的下一个元素的存储内容
	node1=Node("data3",node3)
	print(node1.next.next.data)
