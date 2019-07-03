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
def search_by_data(head,search_data):
	probe=head#获取头节点
	while probe!=None and search_data!=probe.data:#当next不为空，且搜索数据与存储数据不一致时，则访问链表下一个元素
		probe=probe.next
	if probe!=None:#找到数据了
		print("We got the data",probe.data)
	else:#因为搜索到None而推出，则搜索失败
		print(search_data,"not in list")
def search_by_ith_item(head,i):
	probe=head
	for x in range(i):
		probe=probe.next
	if probe==None:
		print("Error index")
	else:
		print(probe.data)
if __name__=="__main__":
	head_node=test_node()
	print("iter node!")
	iter_node(head_node)
	print("")
	search_by_data(head_node,'data5')
	search_by_data(head_node,'data7')
	search_by_ith_item(head_node,5)
	search_by_ith_item(head_node,2)
