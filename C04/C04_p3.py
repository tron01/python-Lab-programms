#Create a class Rectangle with private attributes length and width. 
# Overload ‘<’ operator to compare the area of 2 rectangles.

class rectangle:
    def __init__(self):
        self.__length=int(input("length:"))
        self.__breadth=int(input("breadth:"))
    def __lt__(self,ob2):
        area1=self.__length * self.__breadth
        area2=ob2.__length *ob2.__breadth
        print("the area1:",area1)
        print("the area2:",area2)
        return (area1<area2)
print("Rectangle-1")
og1=rectangle()
print("Rectangle-2")
og2=rectangle()

print(og1<og2)

if og1<og2:
    print("rectangle 1 is smaller")
else:
    print("rectangle 2 is smaller")