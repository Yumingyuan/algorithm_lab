# -*- coding: utf-8 -*-
def takefirst(elem):
	return elem[1]#返回在A上的执行时间		
def takesecond(elem):
	return elem[2]#返回在B上的执行时间
def calc_jobs_cost(jobs_a,jobs_b):
	total_cost=0
	temp_calc=0
	for i in range(len(jobs_a)):
		temp_calc+=jobs_a[i][1]
		if temp_calc>total_cost:
			total_cost=temp_calc
		total_cost+=jobs_a[i][2]
	for i in range(len(jobs_b)):
		temp_calc+=jobs_b[i][1]
		if temp_calc>total_cost:
			total_cost=temp_calc
		total_cost+=jobs_b[i][2]
	print("cost:",total_cost)
def john_calc(job_nums,jobs):
	jobs_a=[]
	jobs_b=[]
	for i in range(job_nums):
		#如果i工件在A设备上工作时间小于在B设备上工作时间
		if jobs[i][1]<jobs[i][2]:
			#将这个job放入jobs_a，根据在A上的工作时间，越短越先进行
			jobs_a.append(jobs[i])
		#如果这个job在B上的工作时间大于在A上的工作时间
		else:
			#将这个job放入jobs_b，根据在B上的工作时间，越短越后进行
			jobs_b.append(jobs[i])
	#jobs_a按在A上工作时间增长的顺序排序
	jobs_a.sort(key=takefirst)
	#jobs_b按在B上工作时间增长的顺序排序
	jobs_b.sort(key=takesecond)
	#将jobs_b元素列表反转，方便正向输出
	jobs_b.reverse()
	print("jobs sequence:",end='')
	#正序输出jobs_a
	for i in range(len(jobs_a)):
		print(jobs_a[i][0],end='')
		print(",",end='')
	#正序输出jobs_b
	for i in range(len(jobs_b)):
		print(jobs_b[i][0],end='')
		if i!=len(jobs_b)-1:
			print(",",end='')
	print("")#换行
	calc_jobs_cost(jobs_a,jobs_b)#调用计算花费函数
if __name__=="__main__":
	#工作列表，第一个是作业编号，第二个是在A上的生产时间，第三个是在B上的生产时间
	jobs=[(1,2,5),(2,4,2),(3,3,3),(4,9,1),(5,1,7)]
	#算法调用
	john_calc(len(jobs),jobs)
