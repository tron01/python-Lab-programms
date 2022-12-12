#Create a list of colors from comma-separated color names entered by user. Display
#first and last colors. 
a=[]
n=int(input("Limit:"))
for i in range(0,n):
    b=input("Enter the color name:")
    a.append(b)
print(a)
print(a[0],a[-1])
