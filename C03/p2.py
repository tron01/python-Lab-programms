"""
create a calculator module having functions suchs as add,sub,multi and div 

write a program to implement to calculator module 

"""

import calculator as c

ch=input("select the operation\na.Add\nb.sub\nc.multiply\nd.Divide\nEnter the choice (a/b/c/d): ")


if ch =="a":
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c.add(a,b)
elif ch =="b":
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c.sub(a,b) 
elif ch =="c":
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c.mult(a,b)
elif ch =="d":
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    c.div(a,b)
else:
    print("Wrong input!")    