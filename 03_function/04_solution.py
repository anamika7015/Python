import math
radius = int(input("enter the radius"))
def area_circumference(radius):
    area = 3.14*radius**2
    circumference = 2*math.pi*radius
    return area,circumference
area,circumference = area_circumference(radius)
print("area of circle:",area,"circumference of circle",circumference)
