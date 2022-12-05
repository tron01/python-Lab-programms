#Find biggest of 3 numbers entered
a=int(input("Enter A:"))
b=int(input("Enter B:"))
c=int(input("Enter C:"))
if a>b:
    if b>c:
        print("A is Greater")
elif b>c:
    print("B is Greater")
else:
    print("C is Greater")        
