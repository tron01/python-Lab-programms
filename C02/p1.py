#Program to find the factorial of a number 
fact=1
n=int(input("Enter the number:"))
if n == 0:
    print("factorial of",n,"is:",fact)
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial of",n,"is:",fact)



