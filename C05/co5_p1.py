#Write a Python program to read a file line by line and store it into a list.
"""
fn = open("demo.txt",'r') #run in thonny  (filename,mode)
s= fn.readline() # for read line by line
print(s)
fn.close()
print(fn.closed)  #file close status
print(fn.mode) #file mode 
print(fn.name) #file name
fo =open("demo2.txt","w")
fo.write("Python is dynamically-typed and garbage-collected \n. It supports multiple programming paradigms")
fo.close()
#replace data in file
f2 =open("demo2.txt","w")
f2.write("Python gdgg")
f2.close()

"""

#fn1 =open("demo2.txt","r")
# read multiple line
"""
s1 =fn1.readline()
s2 =fn1.readline()
s3 =fn1.readline()
print(s1)
print(s2)
print(s3)
"""



"""
for x in range(0,len(s1)):
    print(s1[x])
fn1.close()
"""
"""
#readlines
s1 =fn1.readlines()
print(s1)
"""
 #as list comp

print([line.strip() for line in open('demo2.txt','r')])


