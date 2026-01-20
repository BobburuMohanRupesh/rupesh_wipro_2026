from abc import ABC, abstractmethod

class shape(ABC):
    def display(self):
        print("display method implemented")

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):
    def area(self):
        print("area method implemented")

r = Rectangle()
r.display()
r.area()

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Bull(Animal):
    def sound(self):
        print("Roar")
bull = Bull()
bull.sound()