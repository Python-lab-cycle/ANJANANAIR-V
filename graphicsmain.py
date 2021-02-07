from graphics.rectangleAPFunction import*
from graphics.CircleAPFunction import*
from graphics.dgraphics.cuboidAPFunction import*
from graphics.dgraphics.sphereAPFun import*


num1=int(input("enter length of rectangle"))
num2=int(input("enter breadth of a rectangle"))
print("area = ",Recarea(num1,num2))
print("perimeter =",Rperimeter(num1,num2))


radius=int(input("enter the radius of a circle"))
print("Circle area =",CArea(radius))
print("Circle perimeter =", CPerimetr(radius))

radius=int(input("enter radius of Sphere"))
print("area of sphere =",Asphere(radius))
print("perimeter of sphere =",Psphere(radius))


edge=int(input("enter the edge of cuboid"))
l=int(input("enter the length of cuboid"))
b=int(input("enter the breadth of cuboid"))
h=int(input("enter the heigth of cuboid"))
print("area of cuboid",Acuboid(edge))
print("perimeter of cuboid",Pcuboid(l,b,h))


