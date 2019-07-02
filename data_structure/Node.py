# -*- coding: utf-8 -*-
class Node(object):
	def __init__(self,data,next=None):
		self.data=data
		self.next=next
def test_node():
	for count in range(1,6):
		head=Node('data'+str(count),head)
	return head
def iter_node(head):
	while head!=None:
		print(head.data)
		head=head.next
if __name__=="__main__":
	head_node=test_node()
	iter_note(head_node)
