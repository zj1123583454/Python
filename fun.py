#!/usr/bin/evn python 
#-*-coding:utf-8-*-
def sum(c,d):
	a=c+3
	b=d+4
	print a,b
def str_x():
	global ss  #global字段 将真正的改变变量的值
	ss="Hello"
ss="Hi"
a=3
b=4
sum(a,b)
str_x()
print ss
print a,b
#函数不会改变函数外的ab的值,感觉。。。有点坑

