"""
In this exercise, you will practice overriding a method and using the super() method.

The subclass Cylinder inherits the getArea() method from its superclass Circle. Try overriding the getArea() method in the subclass Cylinder to compute the surface area of the cylinder using the following formula:
surfaceArea = 2 ∗ π ∗ radius * height + 2 ∗ baseArea
That is, if getArea() is called by a Circle instance, it returns the area of the circle. If getArea() is called by a Cylinder instance, it returns the surface area of the cylinder.
When you override the getArea() in the subclass Cylinder, the getVolume() no longer works. This is because the getVolume() uses the overridden getArea() method found in the same class. Please fix the getVolume() method.
You are also required to write a toString() method for the Cylinder class, which overrides the toString() inherited from the superclass Circle. This method will return a string description of the instance in the format: "Cylinder[radius:?, height:?, color:?]"

The code for the Circle and Cylinder classes is automatically included in the answer box. Your task is to update the code of the Cylinder class with:
A new getArea() method
An updated version of the getVolume() method
A new toString() method
"""

import math

'''
The Circle class models a circle with a radius and color.
'''
class Circle:
    # Constructs a Circle instance with default value for radius and color
    def __init__(self, radius = 1.0, color = "red"):
        self.__radius = radius
        self.__color = color
    
    # Getter for radius 
    def getRadius(self):    
        return self.__radius

    # Getter for color     
    def getColor(self):
        return self.__color
    
    # Setter for radius 
    def setRadius(self, radius):
        self.__radius = radius
    
    # Setter for color 
    def setColor(self, color):
        self.__color = color

    # Returns the area of the circle
    def getArea(self):
        return self.__radius * self.__radius * math.pi

    # Returns a String description of the Circle instance
    def __str__(self):
        return f"Circle[radius = {self.__radius}, color = {self.__color}]"

'''
The Cylinder class models a 3D cylinder with a radius, height and color.
'''

class Cylinder(Circle):
    # Constructor a Cylinder instance with default value for radius, height and color
    def __init__(self, radius = 1.0, height = 1.0, color = "red"):
        super().__init__(radius, color)
        self.__height = height

    # Getter for height 
    def getHeight(self):    
        return self.__height
    
    # Setter for height 
    def setHeight(self, height):    
        self.__height = height
    
    # Override method getArea() in the Circle class
    # Returns the surface area of the Cylinder instance

    #########################################################
    # INSERT YOUR CODE FOR getArea() method
    #########################################################
    def getArea(self):
        base_area = super().getArea()
        radius = self.getRadius()
        lateral_area = 2 * math.pi * radius * self.__height
        
        return lateral_area + 2 * base_area

    # Returns the volume of the Cylinder instance
    # Using superclass method getArea() to get the base area

    #########################################################
    # INSERT YOUR CODE FOR getVolume() method
    #########################################################
    def getVolume(self):
        base_area = super().getArea()
        return base_area * self.__height

    # Returns a String description of the Circle instance

    #########################################################
    # INSERT YOUR CODE FOR __str__() method
    #########################################################
    def __str__(self):
        return f"Cylinder[radius:{self.getRadius()}, height:{self.__height}, color:{self.getColor()}]"


    



