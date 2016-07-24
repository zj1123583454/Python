#!/usr/bin/evn python 
#-*-coding:utf=8-*-
from sys import argv
filename=argv[1]
#"r+"的方式既提供读操作也提供写操作,而且写文件是追加的模式
txt=open(filename,"r+")
print "File content:\n",txt.read()
txt.write("I'm Mr.zhang")
txt.close()

txt2=open(filename,"w+") #“w+"的方式打开文件 会把文件内容清空 "r+"不会清空
print ">>",txt2.read() 		#也不会加换行符
txt2.close()
# "a"与"a+"都可以不覆盖原内容对文件进行写操作，区别在于"a"方式不提供读文件操作,而"a+"则提供
txt3=open(filename,"a") 
txt3.write("what")
txt3.close()
txt4=open(filename,"a+")
txt4.write("test!")
txt4.read()
txt4.close()
#注意 如果os.write("xxxx")的下一句紧跟os.read(),那么写操作的”xxx“将不会被
#读取出来，因为只有执行os.close(),文件缓冲区的内容才会被真正的写到文件中
#例如:
txt5=open("./test.txt","r+")
txt5.write("我是测试文件缓冲的")
txt5.read()
txt5.close() #程序运行结果是没有读到任何信息
#但是如果用os.flush()呢?
txt6=open("./test.txt","r+")
txt6.read()
txt6.write("文件已写入")
txt6.flush()
txt6.read()
txt6.close()
#好吧 依然不会立刻读出来.......
