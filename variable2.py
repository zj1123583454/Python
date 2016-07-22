#!usr/bin/evn python
#-*-coding:utf-8-*-
my_name="Mr.zhang"
my_age=20
my_height=74
my_weight=180
my_eyes="black"
my_teeth="White"
my_hair="Brown"
print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height
print "He's %d pounds heavy."%my_weight
print "Actually that's not too heavy."
print "He's fot %s eyes and %s hair." %(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee"%my_teeth
print "If i add %d ,%d ,and %d iget %d " %(my_age,my_height,my_weight,my_age+my_height+my_weight)
print "%r,%r,%r,%r,%r,%r,%r"%(my_name,my_age,my_eyes,my_height,my_weight,my_teeth,my_hair)
#test:
#b=[6.4,7,6,8.2]
#a=round(b)
#print a    Error:居然只能有一个参数。。。。
b=round(8.3)
print b
