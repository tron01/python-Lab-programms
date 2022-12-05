#Create a single string separated with space from two strings by swapping the character at position 1.
s1="food"
s2="good"
print("first string : ",s1)
print("second string: ",s2)
x=s1[0:2]
y=s2[0:2]
s1=s1.replace(s1[0:2],y)
s2=s2.replace(s2[0:2],x)
print("----After swapping----")
print("string :",s1," ",s2)
