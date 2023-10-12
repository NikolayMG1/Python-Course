import math

class Rectangle:

    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.length
    
    def get_color(self):
        return self.color
    
    def calculateArea(self):
        return self.length*self.get_width
    

class Circle:
    def __init__(self, r, color):
        self.r = r
        self.color = color
    
    def get_r(self):
        return self.r
    
    def get_color(self):
        return self.color

    def calculateArea(self):
        return math.pi*self.r*self.r
    

class Shapes(Rectangle, Circle):
    def __init__(self):
        self.rectangles = []
        self.cicrcles = []

    def add_rectangle(self, rectangle):
        self.rectangles.append(rectangle)

    def add_circle(self, circle):
        self.cicrcles.append(circle)

    def sum_all_rectangle(self):
        return sum(Rectangle.calculateArea() for rect in self.rectangles)     

    def sum_all_circles(self):
        return sum(Circle.calculateArea() for circle in self.cicrcles)

    def get_by_index(self, index, type):
        
        if type == Rectangle and len(self.rectangles) > index :
            self.rectangles[index]
        elif type == Circle and len(self.cicrcles) > index :
            self.cicrcles[index]
        else :
            return None