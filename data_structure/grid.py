# -*- coding: utf-8 -*-
from arrays import Array
class Grid(object):
	def __init__(self,rows,columns,fillValue=None):
		self.data=Array(rows)#初始化行
		for row in range(rows):
			self.data[row]=Array(columns,fillValue)#初始化列
			
	def getHeight(self):
		return len(self.data)
	def getWidth(self):
		return len(self.data[0])
