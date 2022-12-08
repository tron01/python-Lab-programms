##Program to find the factorial of a number (Recursion)
def c_fact(x):
    if x == 1:
        return 1
    else:
        return ( x * c_fact(x-1) )

n=int(input("Enter the number:"))
print("factorial of ",n ,"is ",c_fact(n))           