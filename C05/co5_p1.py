#Write a Python program to read a file line by line and store it into a list.

fn = open("demo.txt",'r') #run in thonny  (filename,mode)
s= fn.readline() # for read line by line
print(s) 
print(fn.closed)  #file close status
print(fn.mode) #file mode 
print(fn.name) #file name