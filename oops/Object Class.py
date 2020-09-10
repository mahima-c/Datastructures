

class Circle(object):

	def __init__(self,radius):
		self.__radius = radius

	def __str__(self):
		return "This is a Circle class which takes radius as an argument."

c = Circle(3)
print(c)