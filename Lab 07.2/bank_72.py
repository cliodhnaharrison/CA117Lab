class BankAccount(object):

		def __init__(self, balance=0):
			self.balance = balance
			
		def deposit(self, amount):
			#adds an amount (supplied as an argument) to the balance
			self.amount = amount
			self.balance = self.balance + self.amount
		
		
		
		def withdraw(self, amount):
			#subtracts an amount (supplied as an argument) from the balance 
			#(or says ‘Insufficient funds available’ if withdrawing that amount would cause the balance to go negative)
			self.amount = amount
			self.balance = self.balance - self.amount
			if self.balance < 0:
				self.balance = self.balance + self.amount
				print ("Insufficient funds available")
		
		
		def __str__(self):
			#returns a string describing the current balance
			return 'Your current balance is: {:.2f} euro'.format(self.balance)