class Point(object):

		def __init__(self, x=0, y=0):
			self.x = x
			self.y = y
			
		def distance(self, point2) : 
			#returns the distance between two points (the second point is passed as an argument to the method)
			distance = (((point2.x-self.x)**2) + ((point2.y-self.y)**2))**0.5
			return distance
			
		def __str__(self) : 
			#returns a string describing the point
			return ("({}, {})".format(self.x, self.y))
			
class Segment(object):

		def __init__(self, p1, p2):
			self.p1 = p1
			self.p2 = p2
			
		
		def midpoint(self) : 
			#returns an instance of Point that is the midpoint in the segment
			midpoint = (((self.p1.x + self.p2.x)/2), ((self.p1.y + self.p2.y)/2))
			return midpoint
		
		def length(self) : 
			#returns the length of the segment
			return self.p1.distance(self.p2)
		
class Circle(object):

		def __init__(self, centre, radius):
			self.radius = radius
			self.centre = centre
		
		def overlaps(self, circle2) : 
			#returns True if one Circle overlaps another (passed as an argument) and False otherwise
			if circle2.centre.distance(self.centre) < (self.radius + circle2.radius):
				return True
			else: return False
		