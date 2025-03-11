from math import pi

class Shape:
    def area(self):
        raise NotImplementedError
    
    def circumference(self):
        raise NotImplementedError


class Rectangle(Shape): 
    def __init__( self, x, y, w, h ): 
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def __repr__( self ): 
        return "[({},{}),w={},h={}]".format( self.x, self.y, self.w, self.h )
    
    def area( self ): 
        return self.w * self.h
    
    def circumference( self ): 
        return 2*(self.w + self.h)


class Square(Rectangle):
    def __init__(self, x, y, zijde):
        super().__init__(x, y, zijde, zijde)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __repr__(self):
        return f"({self.x}, {self.y}), r={self.radius}"

    def area(self):
        return pi * self.radius**2
    
    def circumference(self):
        return 2 * pi * self.radius


square = Square(0, 0, 2)
print(square)
circle = Circle(0, 0, 4)
print(circle)
print(circle.area())
print(circle.circumference())