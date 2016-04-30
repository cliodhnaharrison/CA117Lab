#Add es if the noun ends in ch, sh, x, s or z.
#If a noun ends in a consonant + y drop the y and add ies.
#If a noun ends in f (or fe) drop the f (or fe) and add ves.
#If a noun ends in o add es.
#Otherwise add s.

import sys

def plurals():
	s = sys.argv
	word = s[1]
	last = word[-1]
	second_last = word[-2]
	second_last_two = word[-2:]
	vowels = ["a", "e", "i", "o", "u"]
	consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
	if last == "x" or last == "s" or last == "z" or last == "o":
		word = word[0:] + "es"
	elif second_last_two == "ch" or second_last_two == "sh":
		word = word[0:] + "es"
	elif second_last in consonants and last == "y":
		word = word[:-1] + "ies"
	elif last == "f":
		word = word[:-1] + "ves"
	elif second_last_two == "fe":
		word = word[:-2] + "ves"
	else:
		word = word[0:] + "s"
	
		
	print (word)
	
	
	
	
	
plurals()