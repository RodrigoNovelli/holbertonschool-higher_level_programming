#!/ust/bin/pthon3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        if self.radius >= 0:
            return (math.pi * (self.radius ** 2))
        else:
            return (0)


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)
    
    def perimeter(self):
        return 2 * (self.width +  self.height)



def shape_info(Shape):
    area = Shape.area
    print("Area: {}" .format(Shape.area()))
    
    perimieter = Shape.perimeter()
    print("Perimeter: {}" .format(Shape.perimeter()))
