class BankAccount (object):

	next_account_number = 16555232

	def __init__(self, forename, surname, balance):
		self.forename = forename
		self.surname = surname
		self.balance = balance
		self.account_number = self.next_account_number
		BankAccount.next_account_number += 1
		
		
	def lodge(self, amount):
		self.balance += amount
		
	def __str__(self):
		line1 = "Name: {} {}".format(self.forename, self.surname)
		line2 = "Account number: {}".format(self.account_number)
		line3 = "Balance: {:.2f}".format(self.balance)
		return "\n".join([line1, line2, line3])
		
		
class CurrentAccount(BankAccount):

	overdraft = -1000.00
	
	account_type = "current"
	
	def withdraw(self, amount):
		if self.balance - amount >= self.overdraft:
			self.balance -= amount
		else:
			print ("Insufficient funds available")
			
	def __str__(self):
		line4 = "Account type: {}".format(self.account_type)
		return "\n".join([super().__str__(), line4])
		
		
class SavingsAccount(BankAccount):

	interest_rate = 0.01
	
	account_type = "savings"
	
	def apply_interest(self):
		self.balance *= 1 + self.interest_rate
		
	def withdraw(self, amount):
		if self.balance - amount >= 0:
			self.balance -= amount
		else:
			print ("Insufficient funds available")
			
	def __str__(self):
		line4 = "Account type: {}".format(self.account_type)
		return "\n".join([super().__str__(), line4])
		
		
		
		