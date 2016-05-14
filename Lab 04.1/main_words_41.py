import sys
import string


def words():
	file = sys.stdin.read()
	exclude = string.punctuation
	punc = []
	for char in exclude:
		if char == "'":
			pass
		else:
			punc.append(char)
	file = ''.join(char.lower() for char in file if char not in punc).split()

	word_list = {}
	file = sorted(file)
	for word in file:
		if len(word) > 3:
			word_list[word] = file.count(word)
			if int(word_list[word]) < 3:
				del word_list[word]
	sd = sorted(word_list.items())
	
	for key, value in sd:
		print ("{} : {}".format(key, value))
	
words()