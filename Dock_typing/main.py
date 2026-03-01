# Dock typing = Another way to achive polymorphism besides inheritance
#               Object must have the minimum necessary attributes/methods
#               "If it looks like a duck and quacks like a duck. it must be a duck"

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = True

    def speak(self):
        print("HUNK!")

animals = [Dog(), Cat(), Car()]
# error : 'Car' object has no attribute 'speak'
# error ; 'Car' object has no attribute 'alive'
# now my car have minimum necessay attributes and method to cosidered to be animal

for animal in animals:
    animal.speak()
    print(animal.alive)