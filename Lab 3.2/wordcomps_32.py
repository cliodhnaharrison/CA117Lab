import sys

def wordcomps():
	file = sys.stdin.read()
	file = file.strip().split()
	print("Words containing 17 letters: {}".format([n for n in file if len(n) == 17]))
	print("Words containing 18+ letters: {}".format([n for n in file if len(n) > 17]))
	all_vowels = [n for n in file if n.lower().count("a") > 0 and n.lower().count("e") > 0 and n.lower().count("i") > 0 and n.lower().count("o") > 0 and n.lower().count("u") > 0]	
	print("Shortest word containing all vowels: {}".format(min(all_vowels, key = len)))
	print("Words with 4 a's: {}".format([n for n in file if n.lower().count("a") == 4]))
	print("Words with 2+ q's: {}".format([n for n in file if n.lower().count("q") > 1]))
	print("Words containing cie: {}".format([n for n in file if "cie" in n]))
	print("Anagrams of angle: {}".format([n for n in file if n.lower() != "angle" and n.lower().count("a") == 1 and n.lower().count("e") == 1 and n.lower().count("n") == 1 and n.lower().count("g") == 1 and n.lower().count("l") == 1 and len(n) == 5]))
	print("Words ending in iary: {}".format(len([n for n in file if n[-4:] == "iary"])))
	print("Words with q but no u: {}".format([n for n in file if "q" in n.lower() and "u" not in n.lower()]))
	count = 0
	for word in file:
		counting = word.lower().count("e")
		if word.lower().count("e") > count:
			count = counting 
	print("Words with most e's: {}".format([n for n in file if n.lower().count("e") == count]))
	
	
wordcomps()