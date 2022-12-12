#Create a string from given string where first and last characters exchanged. [eg: python -
#> nythop] 

a=input("Enter the string:")
x=list(a)
temp=x[0]
x[0]=x[-1]
x[-1]=temp
print("".join(x))