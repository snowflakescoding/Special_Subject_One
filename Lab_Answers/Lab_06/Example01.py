"""
A class called Circle is designed as shown in the class diagram above. It contains:
Two private instance variables: radius (of the type double) and color (of the type String), with default values of 1.0 and "red", respectively.
Three overloaded constructors - a default constructor with no argument, a constructor that takes a double argument for radius, and a last one takes two arguments for radius and color.
Five public methods: 4 setter and getter methods for radius and color, and getArea(), which returns the radius and area of this instance.
toString() method for string representation of the instance.

Write Python code for the Circle class.
Note: When calculating the area of the circle, you can use the const math.pi from the math library for the π value.
"""

import math

# circle class
class Circle:
    # init function
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    # getter and setter 
    def getRadius(self):
        return self.radius
    
    def setRadius(self, radius):
        self.radius = radius
    
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color
    
    def getArea(self):
        return self.radius * self.radius * math.pi
    
    # string function
    def __str__(self):
        return f"Circle[radius = {self.radius}, color = {self.color}]"
        
