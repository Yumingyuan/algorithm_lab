# -*- coding: utf-8 -*-
class Node(object):
	def __init__(self,data,next=None):
		self.data=data#初始化数据
		self.next=next#初始化next
class TwoWayNode(Node):#继承了Node类的实例化方法
	def __init__(self,data,previous=None,next=None):
		Node.__init__(self,data,next)
		self.previous=previous
if __name__=="__main__":
	head=TwoWayNode(1)#初始化一个链表
	tail=head
	for data in range(2,6):
		tail.next=TwoWayNode(data,tail)
		tail=tail.next#尾插法指向当前创建的双向链表节点
