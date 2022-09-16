from abc import ABC,abstractmethod

class Polygon(ABC):

    @abstractmethod
    def no_of_sides(self):
        pass

class Triangle(Polygon):

    #overloading abstract method
    def no_of_sides(self):
        print("3 sides")

class Pentagon(Polygon):

    def no_of_sides(self):
        print("5 sides")

class Hexagon(Polygon):
    def no_of_sides(self):
        print("6 sides")

class Quad(Polygon):
    def no_of_sides(self):
        print("4 sides")

tri = Triangle()
tri.no_of_sides()

hex = Hexagon()
hex.no_of_sides()
