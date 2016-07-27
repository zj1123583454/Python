#!/usr/bin/evn python
#-*-coding:utf-8-*-
b=["e","f",["G","H"]]
a=["a",["b","c"],"d",b]
print "a的全部元素:",a
print "b的全部元素:",b
for x in a:
	print "遍历a:",x
for x in b:
	print "遍历b:",x

"""循环遍历嵌套的list 嵌套的List只会当作一个元素遍历"""
