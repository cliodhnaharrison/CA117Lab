import sys

def anagrams():
	for line in sys.stdin:
		line = line.strip("\n")
		lines = line.split(" ")
		i = 0
		word_1 = lines[0]
		word_2 = lines[1]
		ana = []
		if len(word_1) != len(word_2):
			ana.append("False")
		for char in lines:
			if word_1[i] in word_2:
				ana.append("True")
			else:
				ana.append("False")
		if "False" in ana:
			print (False)
		else:
			print (True)
		
anagrams()