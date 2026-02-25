# Nested class = A class defied within another class
#                   class Outer:
#                       class Inner:

# Benefits : allow you to logically group classes that are so closely related.
#            Encapsulate private details that are not relevent out side of the outer class
#            keep the namespace clean; Reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        new_empoloyee = self.Employee(name, position)
        self.employees.append(new_empoloyee)

    def list_employee(self):
        # list comprehension
        return [employee.get_details() for employee in self.employees]

def main():
    company1 = Company("Krusty Krab")
    company2 = Company("Chum Bucket")

    company1.add_employee("Eugune", "Manager")
    company1.add_employee("Spongebob", "Cook")
    company1.add_employee("Squidward", "Cashier")

    company2.add_employee("Sheldon", "Manager")
    company2.add_employee("Karen", "Assistant")


    # print(company2.list_employee())
    for employee in company2.list_employee():
        print(employee)

if __name__ == "__main__":
    main()