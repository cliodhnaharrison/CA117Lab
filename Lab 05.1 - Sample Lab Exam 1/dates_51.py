import sys

def dates():
	file = sys.stdin.readlines()
	for line in file:
		line = line.strip().split()
		if line[1] == "January":
			line[1] = 1
		elif line[1] == "February":
			line[1] = 2
		elif line[1] == "March":
			line[1] = 3
		elif line[1] == "April":
			line[1] = 4
		elif line[1] == "May":
			line[1] = 5
		elif line[1] == "June":
			line[1] = 6
		elif line[1] == "July":
			line[1] = 7
		elif line[1] == "August":
			line[1] = 8
		elif line[1] == "September":
			line[1] = 9
		elif line[1] == "October":
			line[1] = 10
		elif line[1] == "November":
			line[1] = 11
		elif line[1] == "December":
			line[1] = 12
		print ("{}/{}/{}".format(line[0], line[1], line[2][2:]))

dates()