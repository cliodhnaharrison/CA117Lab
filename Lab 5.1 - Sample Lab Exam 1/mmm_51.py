import sys
from math import ceil

def mmm():
	file = sys.stdin.read()
	file = file.strip().split()
	total = 0
	for num in file:
		total += int(num)
		
	mean = total / len(file)
	print ("Mean: {:.1f}".format(mean))
	
	mod = {}
	for num in file:
		mod[file.count(num)] = num
	mode = max(mod)
	print ("Mode: {}.0".format(str(mod[mode])))
	
	sfile = sorted(file)
	if len(file) % 2 != 0:
		median = float(sfile[(len(file)//2)])
	else:
		median = (int(sfile[len(file)//2]) + int(sfile[(len(file)//2)-1])) / 2
	print ("Median: {:.1f}".format(median))
mmm()