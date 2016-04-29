import sys
def chop():
	s = sys.argv
	arg = len(s)
	if arg > 1:
		result = s[1]
		if len(result) > 2:
			print (result[1:-1])
chop()

