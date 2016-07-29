#!/usr/bin/evn python
class my_class(object):
	def __init__(self,argv):
		self.argv=argv
	def my_class_print(self):
		for x in self.argv:
			print x.upper()

a=["hello world"]
b=my_class(a)
b.my_class_print()
