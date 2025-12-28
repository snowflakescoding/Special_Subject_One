"""
Write the code for all the classes named Shape, Circle, Rectangle, and Square.
"""

import math

# shape class
class Shape:
    def __init__(self, color: str = "red", filled: bool = True):
        self.color = color
        self.filled = filled

    def getColor(self) -> str:
        return self.color

    def isFilled(self) -> bool:
        return self.filled

    def setColor(self, color: str) -> None:
        self.color = color

    def setFilled(self, filled: bool) -> None:
        self.filled = filled

    def __str__(self) -> str:
        return f"Shape[color={self.color},filled={self.filled}]"

# circle subclass
class Circle(Shape):
    def __init__(self, radius: float = 1.0, color: str = "red", filled: bool = True):
        super().__init__(color, filled)
        self.radius = radius

    def getRadius(self) -> float:
        return self.radius

    def setRadius(self, radius: float) -> None:
        self.radius = radius

    def getArea(self) -> float:
        return math.pi * self.radius * self.radius

    def getPerimeter(self) -> float:
        return 2 * math.pi * self.radius

    def __str__(self) -> str:
        return f"Circle[{super().__str__()},radius={self.radius}]"

# rectangle subclass
class Rectangle(Shape):
    def __init__(self, width: float = 1.0, length: float = 1.0, color: str = "red", filled: bool = True):
        super().__init__(color, filled)
        self.width = width
        self.length = length

    def getWidth(self) -> float:
        return self.width

    def getLength(self) -> float:
        return self.length

    def setWidth(self, width: float) -> None:
        self.width = width

    def setLength(self, length: float) -> None:
        self.length = length

    def getArea(self) -> float:
        return self.width * self.length

    def getPerimeter(self) -> float:
        return 2 * (self.width + self.length)

    def __str__(self) -> str:
        return f"Rectangle[{super().__str__()},width={self.width},length={self.length}]"

# square subclass
class Square(Rectangle):
    def __init__(self, side: float = 1.0, color: str = "red", filled: bool = True):
        super().__init__(side, side, color, filled)

    def getSide(self) -> float:
        return self.width

    def setSide(self, side: float) -> None:
        self.width = side
        self.length = side

    def setWidth(self, side: float) -> None:
        self.setSide(side)

    def setLength(self, side: float) -> None:
        self.setSide(side)

    def __str__(self) -> str:
        return f"Square[{super().__str__()}]"
