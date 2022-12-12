
#. Work with built-in packages


import random

#mylist=["Ann","Ben","ciril","John","Eric","Anu"]

#random.shuffle(mylist)
#print(mylist)

import time

#print("Current time in sec :", time.time())

#print("Current  time:", time.ctime())

#print("Current  time after 30 sec:", time.ctime(time.time()+30))

#t=time.localtime()
#print("local time :",t)

#print("current day :",t.tm_mday)

#print("current month :",t.tm_mon)

import calendar

#month =int(input("Enter the month:"))

#year =int(input("Enter the  year:"))
#print(calendar.month(year,month))
#print(calendar.calendar(2022))


import math 

print("value of pi :",math.pi)

import statistics as s

mlist=[1,2,43,5,6,66,77,44]
print("Mean :",s.mean(mlist))
print("Mode :",s.mode(mlist))
print("Median :",s.median(mlist))
print("Harmonic mean :",s.harmonic_mean(mlist))
print("Statistics variance:",s.variance(mlist))
print("Statistics  Median low :",s.median_low(mlist))
