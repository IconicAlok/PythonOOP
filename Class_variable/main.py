# class variable = shared among all instances of a class
#                  Defined outside of the constructor
#                  allow you to share data among all objects created from the class


class Student:

    class_year = 2024
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squidward", 55)
student4 = Student("Sandy", 27)

print(f"My graduating year of {Student.class_year} has {Student.num_student} student")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)

# print(Student.num_student)

# print(student2.class_year)
# class variable can be accessed any one object of that class
# but it's good practise access the variable by the name of the class
# this helps with clearity and readability.
# When we access with class name its more explicit - (class variable)
# print(Student.class_year)