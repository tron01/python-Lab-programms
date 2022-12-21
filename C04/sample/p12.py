

#raise Exception
#l =[10,20,30,49,1]
try:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    if b== 0:
        raise Exception
    c=a/b
    print(c)
    #print(l[5])

except:
    print("Can't divide with zero")
else:
    print("No Exception")
