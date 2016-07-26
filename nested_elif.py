#/usr/bin/evn python 
print "You enter a dark room with two doors.Do you go through door #1 or door #2?"
door=raw_input(">")
if door=='1':
	print "There's a giant bear here eating a cheese cake.what do you do"
	print "1.Take the cake"
	print "2.Scream at the bear"
	beat=raw_input(">")
	if beat=="1":
		print "The eats your face off. Good job!"
	elif beat=="2":
		print "The bear eats your legs off Good job!"
	else:
		print"Well,doing %s is probably better.Bear runs away"%beat
elif door=="2":
	print "You Stare into the endless abyes at Cthulhu's retiana"
	print "1.Blueberries"
	print "2.Yellow jacket clothespins"
	print "3.Understanding revolvers yelling melodies"
	insanity=raw_input(">")	
	if insanity == "1" or insanity == "2":
		print"Your body survives powered by a mind of jello.Good job"
	else:
		print "The insanity rots your eyes into a pool of muck.Good job"
else:
	print "You stumble arund and fall on a knife and die Good job"
	
