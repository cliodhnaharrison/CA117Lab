class Distance(object):
	
	YARDS_PER_MILE = 1760
	
	def __init__(self, miles = 0, yards = 0):
		self.miles = miles
		self.yards = yards
		
	def to_yards(self):
		yards = self.yards
		yards += self.miles * self.YARDS_PER_MILE
		return yards
	
	def __eq__(self, other):
		return (self.miles, self.yards) == (other.miles, other.yards)
		
	def __ne__(self, other):
		return (self.miles, self.yards) != (other.miles, other.yards)
		
	def __gt__(self, other):
		return self.to_yards() > other.to_yards()
		
	def __lt__(self, other):
		return (self.miles, self.yards) < (other.miles, other.yards)
		
	def __ge__(self, other):
		return self.to_yards() >= other.to_yards()
		
	def __le__(self, other):
		return self.to_yards() <= other.to_yards()
		
	def __add__(self, other):
		miles, yards = divmod(self.to_yards() + other.to_yards(), self.YARDS_PER_MILE)
		return Distance(miles, yards)
		
	def __iadd__(self, other):
		self.miles, self.yards = divmod(self.to_yards() + other.to_yards(), self.YARDS_PER_MILE)
		return self
	
	def __radd__(self, other):
		miles, yards = divmod(self.to_yards() + other.to_yards(), self.YARDS_PER_MILE)
		return Distance(miles, yards)
		
	def __mul__(self, other):
		miles, yards = divmod(self.to_yards() * other, self.YARDS_PER_MILE)
		return Distance(miles, yards)
	
	def __imul__(self, other):
		self.miles, self.yards = divmod(self.to_yards() * other, self.YARDS_PER_MILE)
		return self
	
	def __rmul__(self, other):
		miles, yards = divmod(self.to_yards() * other, self.YARDS_PER_MILE)
		return Distance(miles, yards)
		
	def __sub__(self, other):
		miles, yards = divmod(self.to_yards() - other.to_yards(), self.YARDS_PER_MILE)
		if miles < 0:
			return Distance(0, 0)
		return Distance(miles, yards)
		
	def __isub__(self, other):
		self.miles, self.yards = divmod(self.to_yards() - other.to_yards(), self.YARDS_PER_MILE)
		if self.miles < 0:
			return Distance(0, 0)
		return self
	
	
	def __str__(self):
		#0 pound(s) and 0 ounce(s)
		return ("{} mile(s) and {} yard(s)".format(self.miles, self.yards))
	
	@classmethod
	def from_yards(cls, yards):
		return cls(*divmod(yards, cls.YARDS_PER_MILE))