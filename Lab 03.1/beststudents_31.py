import sys

def best_student():
	filename = sys.argv[1]
	try:
		file = open(filename, "r")
		results = []
		dict = {}
		for line in file:
			try:
				words = line.strip().split()
				mar = int(words[0])
				words.remove(words[0])
				nam = ' '.join(words)
				results.append(mar)
				if mar not in dict.keys():
					dict[mar] = nam
				else:
					dict[mar] = dict[mar] + ", " + nam
			except ValueError:
				print("Invalid mark {} encountered. Skipping.".format(words[0]))
				continue
		maxx = max(results)
		name = dict[maxx]
		mark = maxx

		line1 = "Best student(s): {}".format(name)
		line2 = "Best mark: {}".format(mark)
		print("\n".join([line1, line2]))
		
	except FileNotFoundError:
		print('The file {:s} could not be opened.'.format(filename))
		
best_student()