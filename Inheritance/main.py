# Inheritance = allow a class to inharit attribute and method from another class
#               helps with reusability and extensibility
#               class child(Parents), also known as sub(supper)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mickey")

# Although nothing has in Dog class we have still access of attributes and methods the parents class Animal.

print(mouse.name)
print(mouse.is_alive)
mouse.eat()
mouse.sleep()
mouse.speak()

# Even though children class is empty we still inheriting the attributes and methods from the parents