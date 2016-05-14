class Score(object):

		def __init__(self, goals=0, points=0):
			self.goals = goals
			self.points = points
			
			
			
		def greater_than(self, score1): 
			#returns True if one score is greater than another and False otherwise
			if (self.goals + (self.points//3)) > int((score1.goals + (score1.points//3))):
				return True
			else: return False
			
			
			
		def less_than(self, score2): 
			#returns True if one score is less than another
			if (self.goals + (self.points//3)) < int((score2.goals + (score2.points//3))):
				return True
			else: return False
			
			
			
		def equal_to(self, score3): 
			#returns True if one score is equal to another and False otherwise
			if (self.goals + (self.points//3)) == int((score3.goals + (score3.points//3))):
				return True
			else: return False