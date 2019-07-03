# -*- coding: utf-8 -*-
class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
def test_node():#创建链表函数(头部插入法)
	head=None
	for count in range(1,6):
		head=Node('data'+str(count),head)
		print("create node",head)
	return head#返回头节点
def iter_node(head):#遍历链表
	probe=head#获取头指针位置,用临时指针probe遍历节点
	while probe!=None:
		print(probe.data+" ",end='')
		probe=probe.next
if __name__=="__main__":
	head_node=test_node()
	print("iter node!")
	iter_node(head_node)
