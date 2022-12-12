## __init__ = Constructor
## I don't need to make change in between of any Interface(Shape)
## I will just add new class, implement Shape and go on.


import abc


# make a Shape Interface
class Shape(abc.ABC):

    @abc.abstractclassmethod
    def calculateArea(self):
        pass


# rectangular class that implements Shape
class Rectangle(Shape):

    width = 0.0
    height = 0.0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculateArea(self):
        return self.width*self.height

    def setSize(self, w, h):
        self.width = w
        self.height = h


# square class that implements Shape
class Square(Shape):

    side = 0.0

    def __init__(self, side):
        self.side = side

    def calculateArea(self):
        return self.side*self.side

    def setSize(self, s):
        self.side = s
        
        
# circle class that implements Shape
class Circle(Shape):
    
    radius = 0.0
    
    def __init__(self, radius):
        self.radius = radius
        
    def calculateArea(self):
        return pow(self.radius, 2)*3.1416
    
    def setRadius(self, r):
        self.radius = r
    

# areaCalculator class that calculate area of any Shape
class AreaCalculator():

    def calculateArea(self, shape: Shape):
        print("Area is: ", shape.calculateArea())


# main method to test the classes
rectangle = Rectangle(height=10, width=20)
square = Square(side=30)
circle = Circle(radius=15)
areaCalc = AreaCalculator()

rarea = rectangle.calculateArea()
rectangle.setSize(h=20, w=30)
print(rarea)
sarea = square.calculateArea()
square.setSize(50)
print(sarea)
carea = circle.calculateArea()
circle.setRadius(19)
print(carea)


areaCalc.calculateArea(rectangle)
areaCalc.calculateArea(square)
areaCalc.calculateArea(circle)
