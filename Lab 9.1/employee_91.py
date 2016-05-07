class Employee(object):

	def __init__(self, name, number):
		self.name = name
		self.number = number
		
		
	def wages(self):
		if isinstance(self, Manager):
			return Manager.wages(self)
		elif isinstance(self, AssemblyWorker):
			return AssemblyWorker.wages(self)
		else:
			return 0.00
		
	def __str__(self):
		line1 = "Name: {}".format(self.name)
		line2 = "Number: {}".format(self.number)
		line3 = "Wages: {:.2f}".format(Employee.wages(self))
		return "\n".join([line1, line2, line3])
		
class Manager(Employee):

	def __init__(self, name, number, salary):
		super().__init__(name, number)
		self.salary = salary

	def wages(self):
		return self.salary / 52


class AssemblyWorker(Employee):

	def __init__(self, name, number, hourly_rate, hours):
		super().__init__(name, number)
		self.hourly_rate = hourly_rate
		self.hours = hours
		
	def wages(self):
		return self.hourly_rate * self.hours
		