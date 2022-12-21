#__init constructor

"""
find out the cost of rectangular field with breadth =120,length=160.
it cost x (2000) rupees per 1 square unit.

"""
class Rectangle:
    def __init__(self,l,b,cost=0):
        self.length =l
        self.breadth =b
        self.unit_cost =cost
    def perimeter(self):
        return 2 *(self.length + self.breadth)    
    def area(self):
        return self.length *self.breadth
    def calu_cost(self):
        area= self.area()
        return area *self.unit_cost 

r=Rectangle(160,120,2000)
print("area of rectangle: %s cm^2" % (r.area()))
print("cost of rectangle field:Rs %s " % (r.calu_cost()))

