#Write a Python program to read a file line by line and store it into a list.

fn = open("demo.txt",'r') #run in thonny  (filename,mode)
s= fn.readline() # for read line by line
print(s)
fn.close()
print(fn.closed)  #file close status
print(fn.mode) #file mode 
print(fn.name) #file name


fo =open("demo2.txt","w")

fo.write("Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms")
fo.close()

f2 =open("demo2.txt","w")
f2.write("Python gdgg")
f2.close()


