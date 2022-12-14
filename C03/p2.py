"""
create a calculator module having functions suchs as add,sub,multi and div 

write a program to implement to calculator module 

"""

import calculator as c

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

c.add(a,b)
c.sub(a,b)
c.mult(a,b)
c.div(a,b)