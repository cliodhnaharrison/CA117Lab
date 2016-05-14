import sys
import string
from operator import itemgetter

def words():
	file = sys.stdin.read()
	exclude = string.punctuation
	file = ''.join(char.lower() for char in file if char not in exclude).split()
	
	vowels = ["a", "e", "i", "o", "u"]
	vowel_count = {}
	i = 0
	while i < len(vowels):
		count = 0 
		for word in file:
			for char in word:
				if char.lower() == vowels[i]:
					count += 1
			vowel_count[vowels[i]] = count
		i += 1
		
	sd = sorted(vowel_count.items(), key = itemgetter(1), reverse = True)
	
	for key, value in sd:
		print ("{} : {:>3}".format(key, value))
	
words()