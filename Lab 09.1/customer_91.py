class Customer (object):

	discount = 0

	def __init__(self, name, balance, addr_line1, addr_line2, addr_line3):
		self.name = name
		self.balance = balance
		self.addr_line1 = addr_line1
		self.addr_line2 = addr_line2
		self.addr_line3 = addr_line3
		
	def owe(self):
		if isinstance(self, ValuedCustomer):
			return self.balance - (self.balance / 100) * (ValuedCustomer.discount)
		else:
			return self.balance
		
		
	def __str__(self):
		line1 = "{}".format(self.name)
		line2 = "{}".format(self.addr_line1)
		line3 = "{}".format(self.addr_line2)
		line4 = "{}".format(self.addr_line3)
		line5 = "Balance: {:.2f}".format(self.balance)
		if isinstance(self, ValuedCustomer):
			line6 = "Discount: {}%".format(ValuedCustomer.discount)
		else: 
			line6 = "Discount: {}%".format(self.discount)
		line7 = "Amount due: {:.2f}".format(self.owe())
		return "\n".join([line1, line2, line3, line4, line5, line6, line7])
	
	
	
class ValuedCustomer(Customer):

	discount = 10