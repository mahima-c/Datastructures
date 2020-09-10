

class Student:

 # Properties
	name = "Parikh"
	age = 24
	percentage = 80

 # Methods
	def isPassed(self):
		if self.percentage > 40:
			print("Student is Passed")
		else:
			print("Student is not Passed")


s1 = Student()
print(s1.name)
print(s1.percentage)
s1.isPassed()

s2 = Student()
print(s2.name)

a = [1,2,3]
print(type(a))