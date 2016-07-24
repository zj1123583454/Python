#!/usr/bin/evn python 
from sys import argv
script,name=argv
prompt = ">"
print "Hi %s,i'm the ask you a few questions"
print "Do you like me %s "%name
likes=raw_input(prompt)
print "Where do you live %s " %name
lives=raw_input(prompt)
print "What kind of computer do you have?"
computer=raw_input(prompt)
print """
A;right,so you said %r about liking me.
you live in %r .Not sure whrer that is.
And you have a %r computer.nice 
"""%(likes,lives,computer)
