# -*- coding: utf-8 -*-
def takefirst(elem):
	return elem[1]#返回在A上的执行时间		
def takesecond(elem):
	return elem[2]#返回在B上的执行时间
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
	print("jobs sequence:",end='')
	#正序输出jobs_a
	for i in range(len(jobs_a)):
		print(jobs_a[i][0],end='')
		print(",",end='')
	#倒序输出jobs_b
	for i in range(len(jobs_b)-1,-1,-1):
		print(jobs_b[i][0],end='')
		#最后一项不需要输出逗号
		if i!=0:
			print(",",end='')
if __name__=="__main__":
	jobs=[(1,2,5),(2,4,2),(3,3,3),(4,6,1),(5,1,7)]#工作列表
	john_calc(len(jobs),jobs)
