#!/usr/bin/evn python 
#coding:utf-8
import socket
from time import ctime
HOST=""
PORT=8888 #此处尤其注意 端口号需要的是一个数 而不是一个字符串
BUFSIZ=1024
ADDR=(HOST,PORT)
sockfp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockfp.bind(ADDR)
sockfp.listen(5)
while True:
	print "等待连接。。。。。。"
	sockclient,addr=sockfp.accept()
	print "接受连接:",addr
	while True:
		date=""
		date=sockclient.recv(BUFSIZ)
		if not date:
			break
		sockclient.send("[%s] %s"%(ctime(),date))
	sockclient.close()
sockfp.close()
