import sys

def contains():
	s = sys.argv
	arg = len(s)
	i = 0
	contain = False
	if arg > 2:
		substr = s[1]
		string = s[2]

		while i < len(substr):
			if substr[i] not in string:
				contain = False
				
				
			else:
				contain = True
			string = string.replace(substr[i], "")
			i = i + 1
			if contain == False:
				break
		
			
	print (contain)
contains()
