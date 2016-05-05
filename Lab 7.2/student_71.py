class Student(object):
	
		def __init__(self, surname, forename, sid, modlist=[]):
			self.sid = sid
			self.surname = surname
			self.forename = forename
			self.modlist = modlist
			
			
			
		def add_module(self, module) : 
			#adds a module (passed as an argument) to modlist 
			#(has no effect if modlist already contains the module)
			if module not in self.modlist:
				self.modlist.append(module)

			
			
		def del_module(self, module) : 
			#removes a module (passed as an argument) from modlist 
			#(has no effect if the module is not in modlist)
			if module in self.modlist:
				self.modlist.remove(module)

		
		def print_details(self) : 
			#prints student details
			print("ID: {}".format(self.sid))
			print("Surname: {}".format(self.surname))
			print("Forename: {}".format(self.forename))
			print("Modules: " + ' '.join(self.modlist))