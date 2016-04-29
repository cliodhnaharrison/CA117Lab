import sys
def middle():
	s = sys.argv
	if len(s) == 1:
		print ("No middle character!")
	elif (len(s[1])%2 == 0):
		print ("No middle character!")
	else:
		string = s[1]
		length = len(string)		
		print (string[length//2])
	
middle()


