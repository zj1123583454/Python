#/usr/bin evn python 
#-*-coding:utf-8-*-
from sys import argv
filename,src_file,dst_file=argv
print "打开文件%s...."%src_file
src_fp=open(src_file,"r")
print "读取文件%s...."%src_file
src_content=src_fp.read()
print "打开目标文件%s...."%dst_file
dst_fp=open(dst_file,"w+")
print "正在写入%s"%dst_file
dst_fp.write(src_content)
dst_fp.close()
src_fp.close()
print "拷贝完成!\n"
