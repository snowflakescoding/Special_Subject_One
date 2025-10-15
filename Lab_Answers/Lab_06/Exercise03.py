"""
A class called MyTriangle, which models a triangle with 3 vertices and uses three MyPoint instances (created in Exercise 2) as the three vertices, contains:

Three private instance variables v1, v2, v3 (instances of MyPoint), for the three vertices.
Two constructors, a constructor that constructs a MyTriangle with three sets of coordinates, v1 (x1, y1), v2 (x2, y2), v3 (x3, y3). And an overloaded constructor that constructs a MyTriangle given three instances of MyPoint.
A getPerimeter() method that returns the length of the perimeter in double. You should use the distance() method of MyPoint to compute the perimeter.
A method getType(), which prints "Equilateral" if all three sides are equal, "Isosceles" if any two of the three sides are equal, or "Scalene" if the three sides are different.
A toString() method that returns a string description of the instance in the format "MyTriangle[v1=(x1,y1),v2=(x2,y2),v3=(x3,y3)]".

You are required to write code for the MyTriangle class. You should reuse the MyPoint class in Exercise 2.
"""
import math

# MyPoint class from exercise 2
class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def get_x(self):
        return self.x
    
    def set_x(self, x):
        self.x = x
    
    def get_y(self):
        return self.y
    
    def set_y(self, y):
        self.y = y
    
    def get_xy(self):
        return [self.x, self.y]
    
    def set_xy(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def distance(self, *args):
        if len(args) == 0:
            # origin distance
            return ((self.x ** 2) + (self.y ** 2)) ** 0.5
        
        elif len(args) == 1 and isinstance(args[0], MyPoint):
            # distance to another MyPoint instance
            other = args[0]
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        
        elif len(args) == 2:
            # distance to coordinates (x, y)
            x, y = args
            return ((self.x - x) ** 2 + (self.y - y) ** 2) ** 0.5
        else:
            raise ValueError("Invalid arguments for distance()")


# MyTriangle class
class MyTriangle:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.v1 = kwargs.get('v1')
            self.v2 = kwargs.get('v2')
            self.v3 = kwargs.get('v3')
        elif len(args) == 6:
            x1, y1, x2, y2, x3, y3 = args
            self.v1 = MyPoint(x1, y1)
            self.v2 = MyPoint(x2, y2)
            self.v3 = MyPoint(x3, y3)
            
        elif len(args) == 3 and all(isinstance(arg, MyPoint) for arg in args):
            self.v1, self.v2, self.v3 = args
            
        else:
            raise ValueError("Invalid arguments for MyTriangle constructor")
    
    def __str__(self):
        return f"MyTriangle[v1={self.v1}, v2={self.v2}, v3={self.v3}]"
    
    def getPerimeter(self):
        side1 = self.v1.distance(self.v2)
        side2 = self.v2.distance(self.v3)
        side3 = self.v3.distance(self.v1)
        return side1 + side2 + side3
    
    # alias for Python naming convention
    def get_perimeter(self):
        return self.getPerimeter()
    
    def getType(self):
        side1 = self.v1.distance(self.v2)
        side2 = self.v2.distance(self.v3)
        side3 = self.v3.distance(self.v1)
        
        # use small epsilon for floating point comparison
        epsilon = 1e-9
        
        # all three sides are equal (Equilateral)
        if abs(side1 - side2) < epsilon and abs(side2 - side3) < epsilon:
            return "Equilateral"
        # any two sides are equal 
        elif (abs(side1 - side2) < epsilon or 
              abs(side2 - side3) < epsilon or 
              abs(side1 - side3) < epsilon):
            return "Isosceles"
        # all sides are different
        else:
            return "Scalene"
    
    # alias for Python naming convention
    def get_type(self):
        return self.getType()
