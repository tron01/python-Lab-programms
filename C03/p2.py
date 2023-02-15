"""
create a calculator module having functions suchs as add,sub,multi and div 

write a program to implement to calculator module 

"""

import calculator as c

ch=input("select the operation\na.Add\nb.sub\nc.multiply\nd.Divide\nEnter the choice (a/b/c/d): ")

while(ch):
    if ch =="a":
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c.add(a,b)
        ch=input("Enter the choice ")
    elif ch =="b":
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c.sub(a,b) 
        ch=input("Enter the choice ")

    elif ch =="c":
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c.mult(a,b)
        ch=input("Enter the choice ")
    elif ch =="d":
        a=int(input("Enter the first number:"))
        b=int(input("Enter the second number:"))
        c.div(a,b)
        ch=input("Enter the choice ")
    else:
        print("Wrong input!")    