#Form a list of vowels selected from a given word
v=['a','e','i','o','u','A','E','I','O','U']

w=input("Enter the word:")
c=0
for i in w:
    if i in v:
        c=c+1
print(c)
        