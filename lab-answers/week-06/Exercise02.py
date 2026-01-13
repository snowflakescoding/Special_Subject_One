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
    
    def toString(self):
        return f"({self.x},{self.y})"
    
    def __str__(self):
        return self.toString()
    
    def distance(self, x=0, y=0, another=None):
        if another is not None:
            x = another.x
            y = another.y
        
        xDiff = self.x - x
        yDiff = self.y - y
        return math.sqrt(xDiff * xDiff + yDiff * yDiff)


class MyLine:
    def __init__(self, x1=None, y1=None, x2=None, y2=None, begin=None, end=None):
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
        return self.begin.getX()
    
    def setBeginX(self, x):
        self.begin.setX(x)
    
    def getBeginY(self):
        return self.begin.getY()
    
    def setBeginY(self, y):
        self.begin.setY(y)
    
    def getEndX(self):
        return self.end.getX()
    
    def setEndX(self, x):
        self.end.setX(x)
    
    def getEndY(self):
        return self.end.getY()
    
    def setEndY(self, y):
        self.end.setY(y)
    
    def getBeginXY(self):
        return self.begin.getXY()
    
    def setBeginXY(self, x, y):
        self.begin.setXY(x, y)
    
    def getEndXY(self):
        return self.end.getXY()
    
    def setEndXY(self, x, y):
        self.end.setXY(x, y)
    
    def getLength(self):
        return self.begin.distance(another=self.end)
    
    def getGradient(self):
        xDiff = self.begin.getX() - self.end.getX()
        yDiff = self.begin.getY() - self.end.getY()
        return math.atan2(yDiff, xDiff)
    
    def toString(self):
        return f"MyLine[begin={self.begin}, end={self.end}]"
    
    def __str__(self):
        return self.toString()


    

