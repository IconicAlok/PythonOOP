# Object = A bundle of related attributes (variables) and methods (functions).
#           Ex. phone, cup, book
#           You need a class to create many objects

# Class = A (blueprint) used to design the structure and layout of an object

from car import Car

car1 = Car("Mustang",2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

# print(car1)         # Give the memory address of object car1 where it located

# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)

# print(car3.model)
# print(car3.year)
# print(car3.color)
# print(car3.for_sale)

car2.drive()
car2.stop()
car3.describe()