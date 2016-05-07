import math
class Point(object):

	def __init__(self, x, y):
		self.x = x
		self.y = y 
		
	def distance(self, point2):
		distance = (((self.x-point2.x)**2) + ((self.y-point2.y)**2))**0.5
		return distance
	
	
class Shape(object):
	
	def __init__(self, points):
		self.points = points
		
	def sides(self):
		sides = sorted([self.points[i].distance(self.points[i+1]) for i in range(-1, len(self.points)-1)])
		return sides
	
	def perimeter(self):
		perimeter = sum(self.sides())
		return perimeter
	
class Triangle(Shape):

	def area(self):
		a, b, c = self.sides()[0], self.sides()[1], self.sides()[2]
		s = (a + b + c) / (2)
		area = s * ((s - a) * (s - b) * (s - c))
		area = math.sqrt(area)
		return area

class Square(Shape):

	def area(self):
		a, b, c, d = self.sides()
		area = a * b
		return area
		
		
