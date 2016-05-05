import sys


def evil_words():
	file = sys.stdin.read()
	file = file.strip().split()
	evil = [n for n in file if n.lower().count("e") > 0 and n.lower().count("v") > 0 and n.lower().count("i") > 0 and n.lower().count("l") > 0]
	words = []
	for word in evil:
		evil = ""
		for char in word:
			if char.lower() == "e":
				evil += "e"
			elif char.lower() == "v":
				evil += "v"
			elif char.lower() == "i":
				evil += "i"
			elif char.lower() == "l":
				evil += "l"
			else:
				pass
		#print (evil)
		if evil == "evil":
			words.append(word)
		
	for word in words:
		print (word)
evil_words()