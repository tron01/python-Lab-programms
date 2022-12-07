#Write lambda functions to find area of square, rectangle and triangle.
l=int(input("length "))
b=int(input("breath :"))
h=int(input("heght:"))
ars=lambda x: x*x
arr=lambda x,y:x*y
art=lambda x,y:0.5*x*y
print("Area of square:",ars(l))
print("Area of rectangle:",arr(l,b))
print("Area of triangle:",art(l,h))