#!/usr/bin/evn python 
def add(a,b):
	print "Adding:%d+%d"%(a,b)
	return a+b

def subtact(a,b):
	print "Subtracting:%d-%d"%(a,b)
	return a-b

def multiply(a,b):
	print "Multiplying:%d*%d"%(a,b)
	return a*b
def dicide(a,b):
	print "Dividing %d/%d"%(a,b)
	return a/b
print "Let't go:\n"

sum1=add(30,5)
sum2=subtact(78,4)
sum3=multiply(90,2)
sum4=dicide(100,2)
print """sum1
sum2
sum3
sum4"""
what=add(sum1,subtact(sum2,multiply(sum3,dicide(sum4,2))))
print "That becomes:%d"%what,"can you do it by hand?"

