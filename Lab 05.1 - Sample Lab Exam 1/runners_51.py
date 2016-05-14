import sys


def time_to_seconds(minutes, seconds):
	result = minutes*60
	result += seconds
	return result
	
def seconds_to_time(seconds):
	minutes = str(seconds // 60)
	seconds = str(seconds % 60)
	if len(seconds) == 1:
		seconds = "0" + seconds
	else:
		pass
	original_time = minutes + ":" + seconds
	return original_time
	
def runners():
	file = sys.stdin.readlines()
	mini = []
	names = []
	for line in file:
		times = []
		
		line = line.strip().split()
		name = line[0]
		times_string = line[1:]
		for time in times_string:
			try:
				minutes = int(time.split(':')[0])
				seconds = int(time.split(':')[1])
				min_time = time_to_seconds(minutes, seconds)
				times.append(min_time)
				names.append(name)
			except:
				times = []
				names.remove(name)
				break
	
		if times != []:
			mini.append(min(times))
	best_time = min(mini)
	index = mini.index(best_time)
	best_name = names[5*index]
	best_time = seconds_to_time(best_time)
	print ("{} : {}".format(best_name, best_time))

runners() 