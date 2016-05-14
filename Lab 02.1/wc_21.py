import sys

def word_count():
	file = sys.stdin.read()
	input = file.split()
	print (len(input))
	
word_count()