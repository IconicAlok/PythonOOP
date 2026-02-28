# Abstract class = A class that can not be instantiated on its own; Meant to be subclassed.
#                  They can contain abstract method, which are decleared but have no implementation.
#                  Abstract classed benifits
#                  1. Prevents instantiation of the class itself
#                  2. Requires children to used inherited abstract method

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")


    def stop(self):
        print("You stop the motorcycle")

class Boat(Vehicle):
    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boad")



# vehicle = Vehicle()
                              # error = Can't instantiate abstract class Vehicle without an implementation for abstract methods 'go', 'stop'
car = Car()                   # When inherit from abstruct class, must be implement their abstract method also. Otherwise error
motorcycle = Motorcycle()
boat = Boat()

boat.go()
boat.stop()