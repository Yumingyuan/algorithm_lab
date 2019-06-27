# -*- coding: utf-8 -*-
class Array(object):
	def __init__(self,capacity,fillValue=None):#capacity是数组荣来那个
		self.items=[]
		for count in range(capacity):
			self.items.append(fillValue)
	def __len__(self):
		return len(self.items)#返回list尺寸
	def __str__(self):
		return str(self.items)#返回字符串形式
	def __iter__(self):
		return iter(self.items)#返回迭代器形式
	def __getitem__(self,index):
		if index>=len(self.items):
			return 0
		return self.items[index]
	def __setitem__(self,index,newitem):
		if index>=len(self.items):
			print("Error set index!",index,"the array length is:",len(self.items))#错误提示
			return
		else:
			self.items[index]=newitem
if __name__=="__main__":
	a=Array(5,50)#实例化
	print("length:",len(a))
	print("content:",a)
	for i in range(len(a)):
		a[i]=i+1
	print("after replace content:",a)
	a[5]=5#无效的访问index，代码会提示错误
	print("iter result:")
	for item in a:#按照__iter__遍历
		print(item)#输出每个迭代的元素
	a[4]=100
	print("after replace content:",a)
