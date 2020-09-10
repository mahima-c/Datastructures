# class Student:
#     name = "mahima"
#     def store_details(self):
#         self.age = 60
#     def print_details(self):
#         print(self.name, end=" ")
#         print(self.age)
# s = Student()
# s.store_details()
# s.print_details()
# class StudentD:
#     name = "Parikh"
#     def store_details(self):
#         self.age = 60
#     def print_age(self):
#         print(self.age)
# s = StudentD()
# s.store_details()
# s1 = StudentD()
# s1.print_age()
class Student:

    def __init__(self,name,age):
        self.name = "Rohan"
        self.age = 20

    def print_student_details():
        print(self.name, end= "")
        print(self.age)


# s = Student()
# s.print_student_details()
# s1 = Student("Parikh",25)
# s1.print_student_details()

class Student1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_student_details():
        print(self.name)
        print(self.age)

    @staticmethod
    def isTeen(age):
        return age>16

# a = Student1.isTeen(18)
Student1.print_student_details()
# print(a)