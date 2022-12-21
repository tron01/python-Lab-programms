#try catch divide by zero

try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b

except:
    print("Can't divide with zero")
else:
    print("No error")
finally:
    print("the ' try except ' is finished ")