class Contact(object):

	def __init__(self, name, phone, email):
		self.name = name
		self.phone = phone
		self.email = email

	def __str__(self):
		return ("{} {} {}".format(self.name, self.phone, self.email))

class ContactList(object):

	def __init__(self):
		self.d = {}
	
	def add_contact(self, contact): 
		#adds a new Contact to the contact list (or updates an existing Contact if already present)
		self.d[contact.name] = contact

	def del_contact(self, name): 
		#removes a Contact from the contact list (no effect if no such contact exists)
		if name in self.d:
			del self.d[name]
		
	def get_contact(self, name): 
		#returns a string with the specified contact’s details (or ‘No such contact’ if not in the contact list)
		if name in self.d:
			return str(self.d[name])
		else: return name + " : No such contact"
		

	def __str__(self) : 
		#returns a string containing all contacts’ details listed in alphabetical order 
		#(it should make use of each contact’s __str__() method in order to do so)
		line1 = "Contact list"
		line2 = "-" * len(line1)
		sorted_contacts = [str(self.d[x]) for x in sorted(self.d)]
		return "\n".join([line1, line2, "\n".join(sorted_contacts)])