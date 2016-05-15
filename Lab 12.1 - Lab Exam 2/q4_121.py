class BankAccount (object):

	next_account_number = 18555666

	def __init__(self, name, balance, transactions = []):
		self.name = name
		self.balance = balance
		self.transactions = ['Opening balance: {:.2f}'.format(balance)]
		self.account_number = self.next_account_number
		BankAccount.next_account_number += 1
		
	
	def add_transaction(self, transaction):
		self.transactions.append(transaction)
		
	
	def print_statement(self):
		line1 = "Statement"
		line2 = "-" * len(line1)
		line3 = "\n".join(self.transactions)
		line4 = "Current balance: {:.2f}".format(self.balance)
		print ("\n".join([line1, line2, line3, line4]))
		
	def lodge(self, amount):
		self.balance += amount
		self.add_transaction("Lodgement: {:.2f}".format(amount))
		
	def __str__(self):
		line1 = "Name: {}".format(self.name)
		line2 = "Account number: {}".format(self.account_number)
		line3 = "Balance: {:.2f}".format(self.balance)
		return "\n".join([line1, line2, line3])
		
		
class CurrentAccount(BankAccount):

	overdraft = 2000.00
	
	account_type = "Current account"
	
	def withdraw(self, amount):
		if self.balance - amount >= -(self.overdraft):
			self.balance -= amount
			self.add_transaction("Withdrawal: {:.2f}".format(amount))
		else:
			print ("Insufficient funds available")
			
	def __str__(self):
		line4 = "{}".format(self.account_type)
		return "\n".join([line4, super().__str__()])
		
		
class SavingsAccount(BankAccount):

	interest_rate = 0.05
	
	account_type = "Savings account"
	
	def apply_interest(self):
		self.add_transaction("Interest: {:.2f}".format(self.balance * self.interest_rate))
		self.balance *= 1 + self.interest_rate
		
		
	def withdraw(self, amount):
		if self.balance - amount >= 0:
			self.balance -= amount
			self.add_transaction("Withdrawal: {:.2f}".format(amount))
		else:
			print ("Insufficient funds available")
			
	
	def __str__(self):
		line4 = "{}".format(self.account_type)
		return "\n".join([line4, super().__str__()])