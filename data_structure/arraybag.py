from arrays import Array
class ArrayBag(object):
	DEFAULT_CAPACITY=10#默认长度
	def __init__(self,sourceCollection=None):
		self.item=Array(ArrayBag.DEFAULT_CAPACITY)#初始化Array对象
		self.size=0
		if sourceCollection:
			for i in sourceCollection:
				self.item.add(i)
if __name__=="__main__":
	hi=[1,3,4,5,7]
	a=ArrayBag(hi)
	print(a)
