import sys
import string

def palindromes():
	s = sys.argv
	w = s[1]
	w = w.lower()
	exclude = set(string.punctuation)
	w = ''.join(ch for ch in w if ch not in exclude)
	w = w.replace(" ", "")
	return w == w[::-1]
	
print(palindromes())