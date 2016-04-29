import sys

def conv2decimal():
	s = sys.argv
	arg = s[1]
	base = s[2]
	base = int(base)
	num = int(arg, base = base)
	print (num)
	
conv2decimal() 