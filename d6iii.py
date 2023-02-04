#write a program that has class named circle use a class variable to define the values of a constant pi.use this class variable to calculate area and circumference of the circle to specify the radius
class Circle:
    PI = 3.14
    
    def __init__(self, radius):
        self.radius = radius
        
    def area (self):
        return (Circle.PI * self.radius * self.radius)
    
    def circumference(self):
        return (2 * Circle.PI * self.radius)

r = int(input("Enter the radius of circle"))
c1 = Circle(r)
print ("The area of C1 circle is: ", c1.area())
print ("Circumference of C1 Circle is: ", c1.circumference())
print("")
r = int(input("Enter the radius of circle"))
c2 = Circle(r)
print ("Area of C1 circle is: ", c2.area())
print ("Circumference of C1 Circle is: ", c2.circumference())