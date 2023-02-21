#Accept a list of words and return length of longest word

a=[]
n=int(input("enter the number"))
for i in range(n):
    b=input("enter the value")
    a.append(b)
print(a)
m=len(a[0])
temp=a[0]
for i in a:
    if (len(i)>m):
        m=len(i)
        temp=i
print("longest word is",temp, "and length is ",m) 