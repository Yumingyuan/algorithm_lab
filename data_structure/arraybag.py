from arrays import Array
class ArrayBag(object):
	DEFAULT_CAPACITY=10#默认长度
	def __init__(self,sourceCollection=None):
		self.item=Array(DEFAULT_CAPACITY)#初始化Array对象
