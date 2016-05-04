import sys

def contacts():
	file = sys.argv[1]
	f = open(file, 'r')
	
	contacts = {}
	for line in f:
		file = line.strip()
		name = []
		number = []
		for char in file:
			if char.isalpha() == True:
				name.append(char)
			if char.isalpha() == False:
				number.append(char)
		contacts["".join(name)] = "".join(number)

	names = sys.stdin.readlines()
	for line in names:
		line = line.strip()
		if line in contacts:
			print ("Phone:{}".format(contacts[line]))
		else:
			print ("No such contact")
	
contacts()