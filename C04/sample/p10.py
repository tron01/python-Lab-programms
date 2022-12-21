#try catch divide by zero

try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b

except Exception as e:
    #print("Can't divide with zero")
    print(e)
else:
    print("No Exception")
finally:
    print("the ' try except ' is finished ")