# -*- coding: utf-8 -*-
import copy
import time
def last_item(list_item):
	return list_item[len(list_item)-1]
class Bound_Road:
	"""分支限界计算类"""
	current_path=[]#当前的经过的路径
	current_path.append(0)
	#path.append(0)#一定经过起始点
	optimal_path=[]#最优路径
	current_path_length=0#当前路径的长度
	optimal_path_length=9999#符合要求的最优路径长度
	current_cost=0#当前路径的养路费
	optimal_cost=1500#符合要求的最优养路费（上界）
	length_list=[]#原始矩阵m1，长度list
	value_list=[]#原始矩阵m2，费用list
	softed_length_list=[]#经过松弛后的长度list
	shortest_length=[]#从0到49号节点到49号节点（终点）的最短距离
	def read_data_from_file(self):#读取m1和m2
		f1=open("m1.txt","r")
		f2=open("m2.txt","r")
		for line in f1:
			line_split=line.strip('\n').split('\t')#去掉结尾的\n并把每行内容按\t分开
			line_split=[int(num) for num in line_split]
			self.length_list.append(line_split)
		for line in f2:
			line_split=line.strip('\n').split('\t')#去掉结尾的\n并把每行内容按\t分开
			line_split=[int(num) for num in line_split]
			self.value_list.append(line_split)
	def floyd_for_length(self):#松弛临接矩阵
		self.softed_length_list=[[0 for i in range(len(self.length_list[0]))] for i in range(len(self.length_list))]#生成一个与length_list大小匹配的二维列表，为后续深拷贝打基础
		self.softed_length_list=copy.deepcopy(self.length_list)#把length_list深度拷贝到update_length_list
		for i in range(len(self.softed_length_list)):
			for j in range(len(self.softed_length_list)):
				for k in range(len(self.softed_length_list)):
					if self.softed_length_list[i][j]>self.softed_length_list[i][k]+self.softed_length_list[k][j]:
						self.softed_length_list[i][j]=self.softed_length_list[i][k]+self.softed_length_list[k][j]
	def calc_lower_bound(self):#计算经过松弛之后到乙点的最小距离
		for i in range(len(self.softed_length_list)-1):
			self.shortest_length.append(self.softed_length_list[i][49])
		self.shortest_length.append(0)#乙到自己的距离为0
	def check_optimal(self,i):
		if self.current_path[-1]>=i:#如果当前扩展节点与搜索节点相同，则无需搜索
			return False
		if self.length_list[self.current_path[-1]][i]==9999:#当亲扩展节点到i不可达
			return False
		if  self.length_list[self.current_path[-1]][i]+self.current_path_length+self.shortest_length[i]>self.optimal_path_length:#当前扩展节点到i点的距离加上目前的最短路长度加从i到终点的距离大于最优值
			return False
		if self.value_list[self.current_path[-1]][i]+self.current_cost>1500:#当前扩展节点到i点的距离加上目前的最短路花费以大于上限，肯定不能要了
			return False
		return True
	def bound_search(self):
		if self.current_path[-1]==49:#current_path的最后一个元素是乙节点
			self.optimal_path_length=self.current_path_length#最优秀的长度
			self.optimal_cost=self.current_cost#最优花费
			self.optimal_path=copy.deepcopy(self.current_path)#路径
			return 
		#还没到乙
		for j in range(49,-1,-1):#从后往前遍历搜索节点
			if self.check_optimal(j):
				self.current_path_length+=self.length_list[self.current_path[-1]][j]
				self.current_cost+=self.value_list[self.current_path[-1]][j]
				self.current_path.append(j)
				self.bound_search()#递归调用
				self.current_path.pop()
				self.current_path_length-=self.length_list[self.current_path[-1]][j]
				self.current_cost-=self.value_list[self.current_path[-1]][j]
if __name__=="__main__":
	x=Bound_Road()#实例化对象
	x.read_data_from_file()#读取m1和m2
	x.floyd_for_length()#松弛m1,得到到乙的最短距离作为下界
	x.calc_lower_bound()#计算所有节点到乙点最小距离和花费
	time1=time.time()#搜索起始时间
	x.bound_search()
	time2=time.time()#搜索结束时间
	print("Time:",(time2-time1))
	print("Path length:",x.optimal_path_length)
	print("Path Cost:",x.optimal_cost)
	print("optimal path:",[i+1 for i in x.optimal_path])
	
