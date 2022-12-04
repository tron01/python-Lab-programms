#Prompt the user for a list of integers. For all values greater than 100, store ‘over’ instead

l=[]
for i in range(0,5):
    n=int(input("Enter the integers:"))
    l.insert(i,n)
    if l[i]>100:
        l[i]="over"
print(l)