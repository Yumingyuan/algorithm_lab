# -*- coding: utf-8 -*-
from arrays import Array
class Grid(object):
	def __init__(self,rows,columns,fillValue=None):
		self.data=Array(rows)#初始化行
		for row in range(rows):
			self.data[row]=Array(columns,fillValue)#初始化列		
	def getHeight(self):#获取行数
		return len(self.data)
	def getWidth(self):#获取列数
		return len(self.data[0])
	def __getitem__(self,index):
		return self.data[index]
	def __str__(self):
		result=""
		for row in range(self.getHeight()):
			for col in range(self.getWidth()):
				result+=str(self.data[row][col])+" \n"
		return result
if __name__=="__main__":
	matrix=Grid(3,3,3)
	print(matrix[0])
				
