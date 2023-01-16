#Create a class Time with private attributes hour, minute and second.
#  Overload ‘+’ operator to find sum of 2 time.

class Time:
    def __init__(self):
        self.__h=int(input("Enter the hour:"))
        self.__m=int(input("Enter the minute:"))
        self.__s=int(input("Enter the second:"))
    def __add__(self,time2):
        hour =self.__h + time2.__h

        minute =self.__m + time2.__m
        
        second  =self.__s + time2.__s
        if hour >=24:
            hour=hour%24
        if minute >=60:
            hour =hour+int(minute/60)
            minute=minute%60   
        if second >=60:
            minute =minute + int(second/60)
            second =second%60  
        #return second,minute,hour
        print("sum of Hours:",hour)
        print("sum of minute:",minute)
        print("sum of second:",second)
                 

print("Time of first object")
time1=Time()
print("Time of second object")   
time2=Time()    
print("-------------------")    
time1.__add__(time2)
print("-------------------")    