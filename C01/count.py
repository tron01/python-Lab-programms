#. Count the occurrences of each word in a line of text. 


#The split() method splits a string into a list.
w=(input("Enter the text:").split())
a={i:w.count(i) for i in w}
print(a)
