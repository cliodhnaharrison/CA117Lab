import sys
def substring():
	s = sys.argv
	arg = len(s)
	if arg > 2:
		string = s[1]
		substr = s[2]
		if substr in string:
			print (True)
		else:
			print (False)
substring()
