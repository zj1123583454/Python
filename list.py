#!/usr/bin/evn ptthon 
#-*-coding:utf-8-*-
list_a=["a","b","c","d","e"]
list_b=[]
for i in list_a:
	list_b.append(i)
print list_b
for x in range(0,3):
	list_a.insert(x,x)
print list_a

list_b.pop(-1)
print list_b
list_b.pop(0)
print list_b

'''list_.pop(x) 删除list的x位置元素
	 list.insert(x,y)把x插入到list的y的位置
	 list.append(x)把x追加到list的末尾'''
