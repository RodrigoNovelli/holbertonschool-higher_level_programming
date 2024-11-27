#!/usr/bin/python3
import math
class Shape:
    def area():
        raise NotImplementedError ("This method should be implemented in a subclass")
    
class Circle(Shape):
    def __init__(self, radio: int):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

