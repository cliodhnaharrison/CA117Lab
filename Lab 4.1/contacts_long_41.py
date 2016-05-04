import sys

def contacts():
	file = sys.argv[1]
	f = open(file, 'r')

	contacts = {}
	for line in f:
		file = line.strip()
		name = []
		number_and_email = []
		for char in file:
			if char.isalpha() == True:
				name.append(char)
			if char.isalpha() == False:
				index = line.index(char[-1])
				number_and_email = line[index:-1]
				break
		contacts["".join(name)] = "".join(number_and_email)
	
	names = sys.stdin.readlines()

	for line in names:
		line = line.strip()
		if line in contacts:
			print ("Phone:{}".format(contacts[line][0:12]))
			print ("Email:{}".format(contacts[line][12:]))
		else:
			print ("No such contact")

contacts()