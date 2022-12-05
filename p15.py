#. Print out all colors from color-list1 not contained in color-list2.
l1=["white", "black", "pink"]
l2=["white", "blue", "red"]
u = set(l1).difference(l2)
b=list(u)
print(b)