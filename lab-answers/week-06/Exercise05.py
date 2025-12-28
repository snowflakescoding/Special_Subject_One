"""
A subclass called Cylinder, which models a cylinder, is derived from the superclass Circle (which is created in Example 1). It contains:

Two private instance variables: radius and color, which are inherited from the superclass Circle.
One private instance variable: height with a default value of 1.0.
All public methods are inherited from the superclass Circle.
Four overloaded constructors - a default constructor with no arguments, and three constructors that take arguments for radius, height, and color.
Getter and Setter methods for the height variable.
A getVolume() method, which returns the volume of this Cylinder instance. The formula for calculating the volume of the cylinder is: volume = baseArea ∗ height

You are required to write code for the Cylinder class. You should reuse the Circle class in Example 1.
"""

import math
# Circle class from example 1
class Circle:
    def __init__(self, radius=1.0, color="red"):
        self.radius = radius
        self.color = color

    def getRadius(self):
        return self.radius

    def getColor(self):
        return self.color

    def setRadius(self, radius):
        self.radius = radius

    def setColor(self, color):
        self.color = color
        
    def getArea(self):
        return math.pi * self.radius * self.radius

    def __str__(self):
        return f"Circle[radius={self.radius},color={self.color}]"

# Cylinder - subclass of the Circle 
class Cylinder(Circle):
    def __init__(self, radius=1.0, height=1.0, color="red"):
        super().__init__(radius, color)
        self.height = height

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height

    def getVolume(self):
        return self.getArea() * self.height

