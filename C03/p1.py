
#. Work with built-in packages

#1.a

import random

#mylist=["Ann","Ben","ciril","John","Eric","Anu"]

#random.shuffle(mylist)
#print(mylist)

#1.b

import time

#print("Current time in sec :", time.time())

#print("Current  time:", time.ctime())

#print("Current  time after 30 sec:", time.ctime(time.time()+30))

#t=time.localtime()
#print("local time :",t)

#print("current day :",t.tm_mday)

#print("current month :",t.tm_mon)
#print("current year :",t.tm_year)
#print("current hour :",t.tm_hour)
#print("current minute :",t.tm_min)
#print("current weekday :",t.tm_wday)

#1.c
import calendar

#month =int(input("Enter the month:"))

#year =int(input("Enter the  year:"))
#print(calendar.month(year,month))
#print(calendar.calendar(2022))

#1.d
import math 

#print("value of pi :",math.pi)
from math  import sqrt ,pi
#print("square root of 169:" ,sqrt(169))
#print("value of pi :",math.pi)
#print(math.cos(90))
#print(math.sin(45))

#1.c
import statistics as s

mlist=[1,2,43,5,6,66,77,44]
print("Mean :",s.mean(mlist))
print("Mode :",s.mode(mlist))
print("Median :",s.median(mlist))
print("Harmonic mean :",s.harmonic_mean(mlist))
print("Statistics variance:",s.variance(mlist))
print("Statistics  Median low :",s.median_low([40,55,74,7,-6,78,50]))
