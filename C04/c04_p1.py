#Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
#Compare two Rectangle objects by their area.
class Rectangle:
    
    def __init__(self,l,b,cost=0):
        self.length =l
        self.breadth =b

    def perimeter(self):
        return 2 *(self.length +self.breadth)    
    def area(self):
        return self.length *self.breadth
    def compare(self,r2):
        if r2.area() > r.area():
            print("Area of rectangle 2 is greater")
        elif r2.area() < r.area():
            print("Area of rectangle 1 is greater")
        else:
            print("Both area are Equal")
        
        if r2.perimeter() > r.perimeter():
            print("perimeter of rectangle 2 is greater")
        elif r2.perimeter() < r.perimeter():
            print("perimeter of rectangle 1 is greater")
        else:
            print("Both perimeter are Equal")         
r=Rectangle(10,20)
r2=Rectangle(10,10)
print("Area of 1st rectangle:",r.area())
print("Perimeter of 1st rectangle:",r.perimeter())
print()
print("Area of 2nd rectangle:",r2.area())
print("Perimeter  of 2nd rectangle:",r2.perimeter())
print()
r.compare(r2)