import sys

def diamond():
	s = sys.argv
	stars = s[1]
	stars = int(stars)
	printed = "* "
	i = 1
	space = " "
	spaces = stars - 1
	while i <= stars:
		print (space*(spaces) + (printed*i))
		spaces = spaces - 1
		#Each line must end with a space
		i = i + 1
	if i > int(stars):
		n = stars - 1
		spaces = 1
		while n > 0:
			print (space*(spaces) + (printed*n))
			n = n - 1
			spaces = spaces + 1
			
				
				
					
        
        
        
diamond()

