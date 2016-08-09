#!/usr/bin/evn python
#coding:utf-8
import socket
HOST="192.168.100.103"
PORT=8888
BUFSIZ=1024
ADDR=(HOST,PORT)
sockfp=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
"""此处需要注意:socket.socket() 与sock() 是不同的模块 用法:
sockfp=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
sockfp=socket(AF_INET,SOCK_STREAM,0)
区别在于参数是否加socket."""
sockfp.connect(ADDR)
while True:
	date=""
	date=raw_input(">>")
	if not	 date:
		break
	sockfp.send(date)
	date=""
	date=sockfp.recv(BUFSIZ)
	if not date:
		break
	print date
sockfp.close()

