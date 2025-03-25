# 20.1
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return(f"({self.x}, {self.y})")
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Rectangle:
    def __init__(self, point, width, height):
        self.point = point
        self.width = abs(width)
        self.height = abs(height)
    
    def __repr__(self):
        return(f"{self.point}, w={self.width}, h={self.height}")
    
    def area(self):
        return self.width * self.height
    
    def circumference(self):
        return 2*self.width + 2*self.height

    def bottem_right_corner(self):
        return Point(self.point.x + self.width, self.point.y + self.height)
    
    def overlap(self, rect):
        # werkt niet in alle cases. Wat als er geen overlap is?
        point = Point(rect.point.x, rect.point.y)
        width = self.point.x + self.width - rect.point.x
        height = self.point.y + self.height - rect.point.y
        return Rectangle(point, width, height)


p = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(2, 2)
print(p)
r = Rectangle(p, 4, 4)
r2 = Rectangle(p2, 4, 4)
print(r)
print(r.area(), r.circumference())
print(r.bottem_right_corner())
print(r.overlap(r2))
print(p == p2)
print(p2 == p3)

#test
#test2