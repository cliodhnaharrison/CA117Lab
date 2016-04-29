import sys
def capitals():
	s = sys.argv
	arg = len(s)
	if arg > 1:
		result = s[1]
		if len(result) > 1:
			new = result[1:-1]
			print ((result[0]).upper() + new + (result[-1]).upper())
capitals()

