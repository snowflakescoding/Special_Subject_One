"""
A polyline is a line with segments formed by points. A class called MyPolyLine, which models a polyline and uses a list of MyPoint instances (created in the earlier exercise) as the connection points, contains:

A private list of MyPoint instances for the polyline connection points.
A default constructor that constructs a MyPolyLine with an empty list.
An overloaded constructor that constructs a MyPolyLine with a set of MyPoint instances.
An appendPoint() method that appends a point (x, y) to the end of this polyline.
An overloaded appendPoint() method that appends a MyPoint instance to the end of this polyline.
A getLength() method that returns the total length of all segments of this polyline.
A toString() method that returns a string description of the instance in the format "MyPolyLine{(x1,y1)(x2,y2)(x3,y3)...}".

You are required to write code for the MyPolyLine class. You should reuse the MyPoint class in Exercise 2.
"""

import math
# MyPoint class from exercise 2
class MyPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
    def __str__(self):
        return f"({self.x},{self.y})"

# MyPolyLine class
class MyPolyLine:
    def __init__(self, points=None):
        if points is None:
            self.points = []
        else:
            self.points = list(points)
    
    def appendPoint(self, x=None, y=None, point=None):
        if point is not None:
            self.points.append(point)
        else:
            self.points.append(MyPoint(x, y))  
    
    def getLength(self):
        if len(self.points) < 2:
            return 0
        total_length = 0
        for i in range(len(self.points) - 1):
            total_length += self.points[i].distance(self.points[i + 1])
        return total_length
    
    def __str__(self):
        points_str = "".join(str(point) for point in self.points)
        return f"MyPolyLine{{{points_str}}}"  
