#  user defined Exception for mark

#raise Exception

marks=int(input("Enter A:"))
try:
    if marks< 0 and marks<100:
        raise Exception("Marks should be in between 0 and 100 !")
    print("mark:",marks)    
except Exception as e:
    print(e)

