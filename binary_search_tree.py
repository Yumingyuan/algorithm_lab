# -*- coding: utf-8 -*-
def binary_search(data_list,root,key):
	print("search's root node:",root,"for key:",key)
	if root>=len(data_list):#当搜索的树根节点索引大于树的规模时，未搜索到，返回
		return -1#未查找到结果的情况
	if key==data_list[root]:#当前搜索到的根节点对应的索引值等于key，则返回索引值下标
		return root
	elif key>data_list[root]:#当前搜索到根节点对应的索引值的元素值小于key，则递归查询右子树
		return binary_search(data_list,root*2+1,key)
	else:#当前搜索到根节点对应的索引值的元素值大于key，则递归查询左子树
		return binary_search(data_list,root*2,key)
if __name__=="__main__":
	test_data=[0,16,14,18,13,15,17]#测试数据，是一个二叉查找树
	print("search_data 18:",binary_search(test_data,1,18))#搜索一个已有值
	print("search_data 19:",binary_search(test_data,1,19))#搜索一个树中未存储的值
