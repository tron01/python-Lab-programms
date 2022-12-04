#Form a list of vowels selected from a given word
v=['a','e','i','o','u','A','E','I','O','U']
w=input("Enter the word:")
s=[i for i in w if i in v]
print(s)
print("number of vowels:",len(s))        