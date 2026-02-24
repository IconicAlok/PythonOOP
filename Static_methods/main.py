# Static method = A method thats belog to class rather than many object from that class (instance)
#                   Usually used for general utility functions

# Instances = Best for operations on the instance of that class (object)
# Static method = Best for utility functions that do not nedd to access class data

class Employee:
    def __init__(self, name, position, ):
        self.name = name
        self.position = position

    def getinfo(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        return position in valid_position

employee1 = Employee("Eugune","Manager")
employee2 = Employee("Squidward","Cashier")
employee3 = Employee("Spongebob","Cook")

# print(Employee.is_valid_position("Cook"))
print(Employee.is_valid_position("Rocket Scientist"))
print(employee1.getinfo())
print(employee2.getinfo())
print(employee3.getinfo())