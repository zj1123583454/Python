#!/usr/bin/evn python
#-*-coding:utf-8-*-
# Study Print
# 2016 7.22
# Bad Programmer
print "Hello World!"
print "I'm Bad Progarmmer"
print "I like typeing this."
print "This is fun"
print "Yay! Printing."
print "I'd much rather you 'not'."
print 'I "said"do not not touch this'
print "中文测试","你好 世界!" #显示中文需要采用utf-8编码方式

a="one tow three four"
b="one\ntwo\nthree\nfour\n"
print a
print b
print a,b
print """one
tow
three
four
"""
c=["\"","6'22","6\"22","3\\2","5\\\\2"]
for x in c:
	print "%s\r"%x
#print c 如果这样输出c的内容 字符串的转移字符\不会起作用 只会输出原有的数据
