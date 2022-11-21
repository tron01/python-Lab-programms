#. Count the occurrences of each word in a line of text. 


w=(input("Enter the text:").split())
print(w)
a={i:w.count(i) for i in w}
print(a)
#The split() method splits a string into a list.
