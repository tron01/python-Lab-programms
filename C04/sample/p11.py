#multiple try 
l =[10,20,30,49,1]
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print(c)
    print(l[5])

except ZeroDivisionError:
    print("Can't divide with zero")
except IndexError:
    print("list index ")
