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