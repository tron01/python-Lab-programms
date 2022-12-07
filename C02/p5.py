#Display the given pyramid with step number accepted from user.
#Eg: N=4
#1
#2 4
#3 6 9
#4 8 12 16 

n=int(input("Enter the numbers:"))

for i in range(1,n+1):
    for j in range(0,i+1):
        a=i*j
        if a== 0:
            continue
        else:
            print(a,end=" ")
    print("\n")        
