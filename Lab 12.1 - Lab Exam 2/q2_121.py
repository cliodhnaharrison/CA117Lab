class File(object):
	
	FILE_PERMISSIONS = "rwx"
	
	def __init__(self, name, owner, size = 0, permissions = ""):
		self.name = name
		self.owner = owner
		self.size = size
		self.permissions = permissions
		
	def enable_permission(self, user, mode):
		if self.owner != user:
			print ("Access denied")
			return
		if mode not in self.FILE_PERMISSIONS:
			return
		if mode in self.permissions:
			return
		self.permissions += mode
		
	def disable_permission(self, user, mode):
		if self.owner != user:
			print ("Access denied")
			return
		if mode in self.permissions:
			self.permissions = self.permissions.replace(mode, "")
			
	def has_access(self, user, mode):
		if user == self.owner or mode in self.permissions:
			return "Access granted"
		return "Access denied"
		
	def get_permissions(self):
		if not self.permissions:
			return "null"
		return "".join(sorted(self.permissions))
		
	def get_size(self):
		return self.size
		
	def __str__(self):
		line1 = "File: {}".format(self.name)
		line2 = "Owner: {}".format(self.owner)
		line3 = "Permissions: {}".format(self.get_permissions())
		line4 = "Size: {} bytes".format(self.get_size())
		return "\n".join([line1, line2, line3, line4])

class Folder(object):

	def __init__(self):
		self.d = {}
		#d is a dictionary that maps from the file names to file objects
		
	def add_file(self, f):
		if f.name in self.d:
			print ("File already exists")
			return
		self.d[f.name] = f
		
	def del_file(self, user, name):
		if name not in self.d:
			print ("No such file")
			return
		if self.d[name].owner != user:
			print ("Access denied")
			return
		del self.d[name]
		
	def get_size(self):
		return sum([f.get_size() for f in self.d.values()])
		
	def __str__(self):
		heading = "Folder contents"
		uline = "=" * len(heading)
		slist = [heading,uline]
		for k in sorted(self.d.keys()):
			slist.append(self.d[k].__str__())
		slist.append("Folder size: {} bytes".format(self.get_size()))
		return "\n".join(slist)