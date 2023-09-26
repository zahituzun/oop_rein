from abc import ABC, abstractmethod
#inheritance
class Shape(ABC):
    "Shape = super class / abstact class "

    #abstact method
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # override / polymorhism
    def toString(self):
        pass

class Square(Shape):
    "sub class"
    def __init__(self, edge):
        self.__edge = edge #encapsulation #başka yerlerden erişilemez, private

    def area(self):
        result = self.__edge**2
        print("Square area:",result)

    def perimeter(self):
        result = self.__edge*4
        print("Square perimater:", result)

    #override / polimorphism
    def toString(self):
        print("square edge", self.__edge)

class Circle(Shape):
    #constant variable
    PI = 3.14

    def __init__(self, radius):
        self.__radius = radius


    def area(self):
        result = self.PI * self.__radius ** 2
        print("Circle area:", result)


    def perimeter(self):
        result = 2 * self.PI * self.__radius
        print("Circle perimeter:", result)

    def toString(self):
        print("Circle radius", self.__radius)

c = Circle(5)
c.area()
c.perimeter()
c.toString()

s = Square(5)
s.area()
s.perimeter()
s.toString()




