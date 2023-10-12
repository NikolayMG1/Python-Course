import math
from math import sqrt, sin, cos, atan  # you will need these
from math import pi, isclose  # the tests below will need these



class PolarCoordinate:
    def __init__(self, r, angle):
        self.r = r
        self.angle = angle

    def get_r(self):
        return self.r
    
    def get_angle(self):
        return self.angle
    
    def to_cartesian(self):
        x = self.r*math.cos(self.angle)
        y = self.r*math.sin(self.angle)

        return (x, y)
    
    def from_cartesian(self, x, y):
        self.r = math.sqrt(x*x + y*y)
        self.angle = math.atan(y/x)
        return self

    def __str__(self):
        return f"({self.r}, {self.angle})"

    def __hash__(self):
        return hash((self.r, self.angle)) 
        
    def __eq__(self, other):
        return self.r == other.r and self.angle == other.angle
    
    def __ne__(self, other) -> bool:
        return self.r != other.r or self.angle != other.angle
    

p1 = PolarCoordinate(1, pi/6)

print(p1.r == 1)
print(p1.angle == pi/6)

p2 = PolarCoordinate.from_cartesian(3, 4)
print(isclose(p2.r, 5))
print(isclose(p2.angle, atan(4/3)))

x, y = p2.to_cartesian()
print(isclose(x, 3))
print(isclose(y, 4))

p3 = PolarCoordinate(1, 0)
print(str(p3) == "(r: 1, angle: 0)")
print(repr(p3) == "PolarCoordinate(1, 0)")

pp1, pp2, pp3 = PolarCoordinate(1, pi/6), PolarCoordinate.from_cartesian(3, 4), PolarCoordinate(1, 0)
print(p1 == pp1)
print(p2 == pp2)
print(p3 == pp3)

d = {p1: "A", p2: "B", p3: "C"}
print(d[pp1] == "A")
print(d[pp2] == "B")
print(d[pp3] == "C")

s = {p1, p2, p3, pp1, pp2, pp3, p1, p2, p3}
print(len(s) == 3)
    

