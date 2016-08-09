#!/usr/bin/evb python
class TheThing(object):
	def __init__(self):
		self.number=20
	def some_function(self):
		print "I got called"
	def add_me_up(self,more):
		self.number+=more
		return self.number
a=TheThing()
b=TheThing()
a.some_function()
b.some_function()
print a.add_me_up(20)
print b.add_me_up(80)
print a.number
print b.number
class TheMultiplier(object):
	def __init__(self,besa):
		self.besa=besa
	def do_it(self,m):
		return m * self.besa
x=TheMultiplier(a.number)
print x.do_it(b.number)

