#Generate all factors of a number. 
n=int(input("Enter a number :"))
print(" factors of ",n," are:")
for i in range(0,n):
    for j in range(0,n):
        if i*j==n:
            print(i,j)