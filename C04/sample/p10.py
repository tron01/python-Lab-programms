#try catch divide by zero
#l =[10,20,30,49,1]
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print(c)
    #print(l[5])

except Exception as e:
    #print("Can't divide with zero")
    b=1
    c=a/b
    print(c)
else:
    print("No Exception")
finally:
    print("the ' try except ' is finished ")