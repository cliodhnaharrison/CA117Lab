class Element():
		
		def __init__(self, number, name, symbol, boiling_point):
			self.number = number
			self.name = name
			self.symbol = symbol
			self.boiling_point = boiling_point
			
			
			
		def print_details(self):
			print("Number: {}".format(self.number))
			print("Name: {}".format(self.name))
			print("Symbol: {}".format(self.symbol))
			print("Boiling point: {} C".format(self.boiling_point))
			