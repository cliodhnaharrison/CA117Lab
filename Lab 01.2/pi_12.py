import sys
import math

def pi():
	s = sys.argv
	decimal = s[1]
	print('{:.{}f}'.format(math.pi, decimal))
	
pi()