# Print a formatted league table.

import sys

h1 = 'POS'
h2 = 'CLUB'
h3 = 'P'
h4 = 'W'
h5 = 'D'
h6 = 'L'
h7 = 'GF'
h8 = 'GA'
h9 = 'GD'
h10 = 'PTS'

print('{:>1s} {:20s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:3s}'.format(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10))

for line in sys.stdin:
	line = line.strip("\n")
	lines = line.split(" ")
	POS = lines[0]
	CLUB = lines[1:-8]
	string = ""
	i = 0
	for char in CLUB:
		string = string + " " + CLUB[i] 
		i += 1
	P = lines[-8]
	W = lines[-7]
	D = lines[-6]
	L = lines[-5]
	GF = lines[-4]
	GA = lines[-3]
	GD = lines[-2]
	PTS = lines[-1]
	print(' {:>2s}{:21s} {:2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(POS, string, P, W, D, L, GF, GA, GD, PTS))
	