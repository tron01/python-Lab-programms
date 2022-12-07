#Generate a list of four digit numbers in a given range with all their digits even and the
# number is a perfect square. 
from math import sqrt

n=int(input("Enter a limit:"))
for i in range(1000,n):
    if sqrt(i)== int(sqrt(i)) and i%2==0:
        print(i)
