import sys
import string

def unique():
	file = sys.stdin.read()
	file = file.lower()
	result = ""
	result = ''.join(char for char in file if char not in string.punctuation).split()
	input = set(result)
	print (len(input))
	
unique()

