#. Count the occurrences of each word in a line of text. 


w=(input("Enter the text:").split())
print(w)
for i in range(0,len(w)):
    c=w.count(w[i])
    print("word: ",w[i],":count :",c)


#The split() method splits a string into a list.
