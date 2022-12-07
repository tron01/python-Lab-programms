"""
Construct following pattern using nested loop
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
n=int(input("Enter a limit"))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end=" ")
    print("\n")
for i in reversed(range(0,n)):
    for j in reversed(range(0,i)):
         print("*",end=" ")
    print("\n")