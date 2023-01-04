#Create a class Rectangle with private attributes length and width. 
# Overload ‘<’ operator to compare the area of 2 rectangles.

class Rectangle:
    def __init__(self):
        self.__length=int(input("Enter the length:"))
        self.__width=int(input(("Enter the width:")))
    def __lt__(self,ob2):
        area1=self.__length*self.__width
        area2=ob2.__length*ob2.__width



ob1=Rectangle()
print()
ob2=Rectangle()

if ob1 >ob2:
    print("Rectangle 1 Area is greater")
else:
    print("Rectangle 2 Area is greater")

