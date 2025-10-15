"""
A class called MyPoint, which models a 2D point with x and y coordinates, contains:
Two instance variables x (int) and y (int).
Two constructors, a default constructors that construct a point at the default location of (0, 0). And an overloaded constructor that constructs a point with the given x and y coordinates.
Getters and Setters method for x and y.
A method getXY() which returns the x and y in a 2-element list of int. And a method setXY() to set both x and y.
A toString() method that returns a string description of the instance in the format "(x, y)".
A distance() method that returns the distance from this point to another point at the given (x, y) coordinates, or the given MyPoint instance (called another). The default distance() method returns the distance from this point to the origin (0,0)

A class called MyLine, which models a line with a beginning point at (x1, y1) and an end point at (x2, y2)
You are required to write code for the MyPoint and MyLine classes.
"""

import math

# MyPoint class
class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    def getY(self):
        return self.y
    
    def setY(self, y):
        self.y = y
    
    def getXY(self):
        return [self.x, self.y]
    
    def setXY(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    # calculate the distance between two points
    def distance(self, x=0, y=0, another=None):
        if another is not None:
            dx = self.x - another.x
            dy = self.y - another.y
        else:
            dx = self.x - x
            dy = self.y - y
        return math.sqrt(dx**2 + dy**2)

# MyLine class
class MyLine:
    def __init__(self, x1=0, y1=0, x2=0, y2=0, begin=None, end=None):
        if begin is not None and end is not None:
            self.begin = begin
            self.end = end
        else:
            self.begin = MyPoint(x1, y1)
            self.end = MyPoint(x2, y2)
    
    def getBegin(self):
        return self.begin
    
    def setBegin(self, begin):
        self.begin = begin
    
    def getEnd(self):
        return self.end
    
    def setEnd(self, end):
        self.end = end
    
    def getBeginX(self):
        return self.begin.x
    
    def setBeginX(self, x):
        self.begin.x = x
    
    def getBeginY(self):
        return self.begin.y
    
    def setBeginY(self, y):
        self.begin.y = y
    
    def getEndX(self):
        return self.end.x
    
    def setEndX(self, x):
        self.end.x = x
    
    def getEndY(self):
        return self.end.y
    
    def setEndY(self, y):
        self.end.y = y
    
    def getBeginXY(self):
        return self.begin.getXY()
    
    def setBeginXY(self, x, y):
        self.begin.setXY(x, y)
    
    def getEndXY(self):
        return self.end.getXY()
    
    def setEndXY(self, x, y):
        self.end.setXY(x, y)
    
    # calculate the length and gradient
    def getLength(self):
        return self.begin.distance(another=self.end)
    
    def getGradient(self):
        dx = self.end.x - self.begin.x
        dy = self.end.y - self.begin.y
        return math.atan2(dy, dx)
    
    def __str__(self):
        return f"MyLine[begin={self.begin}, end={self.end}]"


    

