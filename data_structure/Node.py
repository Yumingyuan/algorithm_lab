# -*- coding: utf-8 -*-
class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
def insert_head():#创建链表函数(头部插入法)
	head=None
	for count in range(1,6):
		head=Node('data'+str(count),head)
		print("create node",head)
	return head#返回头节点
def insert_tail(head,data):#尾部插入法
	temp_node=Node(data,None)#创建尾部要放的节点
	if head==None:#如果没有头节点
		head=temp_node#用头节点指向新创建节点
	else:
		probe=head
		while probe.next!=None:
			probe=probe.next#找到尾部
		probe.next=temp_node
		print("Insert at tail:",data)
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
def search_by_ith_item(head,i):#查找链表中的第i项数据，i范围0->n-1
	probe=head
	for x in range(i):
		probe=probe.next
	if probe==None:
		print("Error index")
	else:
		print(probe.data)
def sub_by_data(head,data,sub_data):#搜索data，使用sub_data完成替换
	probe=head
	while probe!=None and data!=probe.data:
		probe=probe.next
	if probe!=None:
		probe.data=sub_data
		return True
	else:
		return False
def sub_by_ith_index(head,i,sub_data):
	probe=head
	for x in range(i):
		probe=probe.next
	if probe==None:
		print("Error index")
	else:
		probe.data=sub_data
		#print("After sub by index:",end='')
		#iter_node(head)#遍历调用
def pop_tail_item(head):
	removed_item=head.data
	if head.next==None:#如果只有一个元素
		head=None
	else:
		probe=head#从头节点开始进行搜索
		while probe.next.next!=None:#如果当前节点的下一个节点的next指向None，则便利到了第n-2项，准备删除第n项
			probe=probe.next#进行next搜索
		removed_item=probe.next.data
		probe.next=None#第n-2项的next设置为None
	return removed_item#返回pop的元素
def pop_item_from_head(head):#从收不删除数据
	removed_Item=head.data
	head=head.next#head指针指向下一个元素
def node_length(head):
	probe=head
	if probe!=None:
		count=1
	else:
		count=0
	while probe!=None:
		count+=1
		probe=probe.next
	return count
def insert_at_ith(head,i,data):#i从0到n-1
	probe=head
	if i>node_length(head) or i<0:
		return
	else:
		if i==0:
			newnode=Node(data)
			newnode.next=probe
			head=newnode#newnode位置作为头节点
			print("")
			print("Insert OK!",data)
			return head
		else:
			for x in range(i-1):#到插入点的前一个位置
				#print(x)
				probe=probe.next
			newnode=Node(data)
			newnode.next=probe.next
			probe.next=newnode
			print("")
			print("Insert OK!",data)#插入成功
			return head#返回经过调整后的链表首部元素地址
def delete_at_ith(head,i):#i从0到n-1
	probe=head
	if i>node_length(head) or i<0:
		return
	else:
		if i=0:
			removed_item=probe.data#获取地一个元素的数据部分
if __name__=="__main__":
	head_node=insert_head()#头部插入法
	print("iter node!")
	iter_node(head_node)
	print("")
	search_by_data(head_node,'data5')#搜索数据为data5的节点
	search_by_data(head_node,'data7')#搜索数据为data3的节点
	search_by_ith_item(head_node,5)#搜索链表第6项
	search_by_ith_item(head_node,2)#搜索链表地3项
	if sub_by_data(head_node,'data3','data8'):#修改data3为data8
		print("After sub by data seach:",end='')
		iter_node(head_node)
		print("")
	else:
		print("No data find! can not sub")
	sub_by_ith_index(head_node,3,"subdatayumingyuan")
	insert_tail(head_node,"tail_insert_data")
	iter_node(head_node)
	result=pop_tail_item(head_node)
	print("\npop for 1 time result:",result)
	iter_node(head_node)#删除一个元素后的遍历
	print()
	insert_at_ith(head_node,3,"tmdaaaa")
	iter_node(head_node)#删除一个元素后的遍历
	head_node=insert_at_ith(head_node,0,"tmdaabb")
	iter_node(head_node)#删除一个元素后的遍历
