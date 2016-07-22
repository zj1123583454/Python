#!/usr/bin/evn python
cars = 100
space_in_a_car=4.0
drivers = 30
passengers = 90 
cars_not_driven= cars-drivers  #70
cars_driven = drivers					 #30
carpool_capacity = cars_driven * space_in_a_car #280.0
average_passengers_per_car = passengers / cars_driven # 3
print "Thhere are",cars,"cars available." #100
print "There are only" ,drivers,"drivers available" # 30
print "There will be ",cars_not_driven,"empty cars today" # 70
print "We can transport",carpool_capacity,"people today" # 280.0
print "We need to put about",average_passengers_per_car,"in each car" #3
