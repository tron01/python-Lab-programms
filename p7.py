#Enter 2 lists of integers. Check
#  (a) Whether list are of same length 
# (b)  whether list sums to same value 
# (c) whether any value occur in both 

l1=[1,2,3,4,5,2]
l2=[1,2,3,4,8,7]
sum=0
sum2=0
if len(l1) == len(l2):
    print("same length")
else:
    print("different length")

for i in l1:
    sum=sum+i
for j in l2:
    sum2=sum2+j
if sum ==sum2:
    print("list sums have same value")
else:
    print("list sums have not same value")

print("whether any value occur in both:")
print("common element")
for x in l1:
    for y in l2:
        if x==y:
            print(y)