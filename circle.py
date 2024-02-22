from math import pi
class Circle:
    def __init__(self,radius) :
        self.radius=radius
    def area(self):
       Area=  pi * self.radius**2
       return Area
    def perimeter(self):
        circum=pi *self.radius*2
        return circum
rad=int(input("Enter the radius:"))
circle1=Circle(rad)
print("The area is" ,circle1.area())
print("the perimeter is",circle1.perimeter())
