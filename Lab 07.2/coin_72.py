
class Coin(object):

		def __init__(self, sideup="Heads"):
			self.sideup = sideup
			
			
			
		def flip(self): 
			#flips the coin after which sideup is random
			import random
			self.sideup = random.choice(["Heads", "Tails"])
			
			
		def getstate(): 
			#returns the current state of sideup
			return self.sideup
		
		
		
		
		def __str__(self): 
			#returns a string describing the current state of the coin
			return "Current state: {}".format(self.sideup)