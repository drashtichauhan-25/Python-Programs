
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self):
        self.__length = 10
        self.__width = 5

    def area(self):
        print("Area of Rectangle:", self.__length * self.__width)

r = Rectangle()
r.area()
