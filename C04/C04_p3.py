#Create a class Rectangle with private attributes length and width. 
# Overload ‘<’ operator to compare the area of 2 rectangles.

class Rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length:"))
        self.__width=int(input(("Enter the width:")))
    def __lt__(self):
        area1=self.__length*self.__width
        return(area1)


ob1=Rectangle()
print()
ob2=Rectangle()

if ob1.__lt__() > ob2.__lt__():
    print("Rectangle 1 Area is greater")
else:
    print("Rectangle 2 Area is greater")

