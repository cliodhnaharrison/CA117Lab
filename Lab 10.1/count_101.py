
def count_letters(s, count=0):
	if s == "":
		return count
	else:
		s = s[1:]
	return count_letters(s, count+1)