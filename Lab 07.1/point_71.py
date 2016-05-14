class Point(object):

		def __init__(self, x=0, y=0):
			self.x = x
			self.y = y 
			
		def reflect(self) : 
			#reflects a point’s coordinates through the origin 
			#(the effect is to simply negate the point’s x and y coordinates)
			self.x = self.x * -1
			self.y = self.y * -1

			
			
		def distance(self, point2) : 
			#returns the distance between two points 
			#(the second point is passed as an argument to the method)
			distance = (((point2.x-self.x)**2) + ((point2.y-self.y)**2))**0.5
			return distance