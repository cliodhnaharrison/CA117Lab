import sys

def best_student():
	filename = sys.argv[1]
	try:
		file = open(filename, "r")
		results = []
		dict = {}
		try:
			for line in file:
				words = line.strip().split()
				mar = int(words[0])
				words.remove(words[0])
				nam = ' '.join(words)
				results.append(mar)
				if mar not in dict.keys():
					dict[mar] = nam
		
			maxx = max(results)
			name = dict[maxx]
			mark = maxx
	
			line1 = "Best student: {}".format(name)
			line2 = "Best mark: {}".format(mark)
			print("\n".join([line1, line2]))
		except ValueError:
			print("Invalid mark {} encountered. Exiting.".format(words[0]))
	except FileNotFoundError:
		print('The file {:s} could not be opened.'.format(filename))
		
best_student()