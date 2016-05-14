#Password security is a problem when users choose passwords that can be easily guessed. 
#Write a Python program that assesses the security of a password by counting the number of character classes it contains. 
#For our purposes there are four character classes: digits, lower case characters, upper case characters and special characters (i.e. everything else).

import sys

def password_security():
	s = sys.argv
	password = s[1]
	type = []
	i = 0
	for char in password:
		character = password[i]
		if character.isnumeric() == True:
			type.append("number")
		if character.isalpha() == True:
			if character.lower() != character:
				type.append("upper letter")
			else: 
				type.append("lower letter")
		elif character.isnumeric() == False and character.isalpha() == False:
			type.append("symbol")
		i = i+1
	type = set(type)
	result = len(type)
	print (result)
	
password_security()

